'''
class Solution(object):
    def letterCombinations(self, digits):
        def generateLetterCombinations(word_list, combinations):
            if not word_list:
                return combinations
            else:
                new_combinations = []
                if not combinations:
                    new_combinations = [letter for letter in word_list[0]]
                
                for letter_w in word_list[0]:
                    for letter_s in combinations:
                        new_combinations.append(letter_s+letter_w)
                del word_list[0]
                final = generateLetterCombinations(word_list, new_combinations)
            return final

        no_2_letter_mapping = {'2':"abc", '3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        digits = '234'
        word_letter_list = [no_2_letter_mapping[digit] for digit in digits]
        all_word_combinations = generateLetterCombinations(word_letter_list, [])
        return all_word_combinations

'''
def generateLetterCombinations(word_list, combinations):
    if not word_list:
        return combinations
    else:
        new_combinations = []
        if not combinations:
            new_combinations = [letter for letter in word_list[0]]
        for letter_w in word_list[0]:
            for letter_s in combinations:
                new_combinations.append(letter_s+letter_w)
        del word_list[0]
        final = generateLetterCombinations(word_list, new_combinations)
    
    return final


if __name__ == "__main__":
    no_2_letter_mapping = {'2':"abc", '3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    digits = '234'
    word_letter_list = [no_2_letter_mapping[digit] for digit in digits]
    #print word_letter_list

    #all_word_combinations = generateLetterCombinations(word_letter_list, [])
    all_word_combinations = generateLetterCombinations(word_letter_list, [])
    print len(all_word_combinations),all_word_combinations
