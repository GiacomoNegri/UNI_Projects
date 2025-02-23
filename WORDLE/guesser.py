from random import choice
import yaml
from rich.console import Console
import math
from wordle import Wordle
from collections import Counter

class Guesser:
    def __init__(self, manual):
        self.word_list = yaml.load(open('dev_wordlist.yaml'), Loader=yaml.FullLoader)
        self._manual = manual
        self.console = Console()
        self._tried = []
        
        self.letter_frequency()
        self.candidates = set(self.word_list)
        self.match_results = {}

        self.first_top_guess = self.best_entropy_guess()
        # print(self.first_top_guess)

    def restart_game(self):
        self._tried = []
        self.candidates = set(self.word_list)

    def letter_frequency(self):
        letter_count = Counter()
        for word in self.word_list:
            letter_count.update(set(word))
        self.letter_freq = letter_count

    def filtering_words(self, x=300):
        freq = {word: sum(self.letter_freq[char] for char in set(word)) for word in self.candidates}
        return [word for word, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:x]]

    def compute_match(self, word, guess):
        counts = Counter(word)
        results = []
        for i, letter in enumerate(guess):
            if guess[i] == word[i]:
                results+=guess[i]
                counts[guess[i]]-=1
            else:
                results+='+'
        for i, letter in enumerate(guess):
            if guess[i] != word[i] and guess[i] in word:
                if counts[guess[i]]>0:
                    counts[guess[i]]-=1
                    results[i]='-'

        return ''.join(results)

    def get_match(self, word, guess):
        if (word, guess) in self.match_results:
            return self.match_results[(word, guess)]
        
        match = self.compute_match(word, guess)
        self.match_results[(word, guess)] = match
        return match

    def eliminate_words(self, used_word, result):
        self.candidates = {word for word in self.candidates if self.get_match(word, used_word) == result}

    def best_entropy_guess(self):
        guess_candidates = self.candidates
        
        top_guess, top_score = None, -float('inf')
        for guess in guess_candidates:
            patterns = Counter(self.get_match(word, guess) for word in self.candidates)
            total_sum = sum(patterns.values())
            entropy = -sum((count / total_sum) * math.log2(count / total_sum) for count in patterns.values() if count > 0)
            
            if entropy > top_score:
                top_score = entropy
                top_guess = guess
        return top_guess
        
    def best_entropy_guess_two_step(self):
        guess_candidates = self.candidates
        top_guess, top_score = None, -float('inf')
    
        for first_guess in guess_candidates:
            first_patterns = Counter(self.get_match(word, first_guess) for word in self.candidates)
            total_first_sum = sum(first_patterns.values())
            
            expected_entropy = 0
    
            for pattern, count in first_patterns.items():
                new_candidates = {word for word in self.candidates if self.get_match(word, first_guess) == pattern}
    
                if not new_candidates:
                    continue
    
                second_guess, second_entropy = None, -float('inf')
                for second_try in new_candidates:
                    second_patterns = Counter(self.get_match(word, second_try) for word in new_candidates)
                    total_second_sum = sum(second_patterns.values())
    
                    entropy = -sum(
                        (count / total_second_sum) * math.log2(count / total_second_sum) 
                        for count in second_patterns.values() if count > 0
                    )
    
                    if entropy > second_entropy:
                        second_entropy = entropy
                        second_guess = second_try
    
                expected_entropy += (count / total_first_sum) * second_entropy
    
            if expected_entropy < top_score:
                top_score = expected_entropy
                top_guess = first_guess
        return str(top_guess)


    def get_guess(self, result):
        if self._manual == 'manual':
            return self.console.input('Your guess:\n')
        else:
            if self._tried:
                self.eliminate_words(self._tried[-1], result)
                # guess = self.best_entropy_guess()
                guess=self.best_entropy_guess_two_step()
            else:
                guess = self.first_top_guess
            
            self._tried.append(guess)
            self.console.print(guess)
            return guess