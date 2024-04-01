class Solver(Wordle):
    def __init__(self):
        super().__init__()
        self.char = [-1]*27
        self.index = [[] for i in range(27)]
        self.index1 = [[] for i in range(27)]

    def generate_guess(self, feedback=None):
        guess = "hello"
        self.char = [-1] * 27
        self.index = [[] for i in range(27)]
        self.index1 = [[] for i in range(27)]
        if feedback != None:
            wd = self.guesses.pop()
            temp = []
            for i in range(5):
                if feedback[i] == 0:
                    self.char[ord(wd[i]) - 96] = 0
                elif feedback[i] == 1:
                    self.char[ord(wd[i]) - 96] = 1
                    self.index1[ord(wd[i]) - 96].append(i)
                    temp.append(wd[i])
                else:
                    self.char[ord(wd[i]) - 96] = 2
                    self.index[ord(wd[i]) - 96].append(i)
                    temp.append(wd[i])
            for pos1 in range(len(self.words)):
                guess_word = self.words[pos1]
                increase_letter_count = [0] * 27
                count_of_similar_letter = [1] * 27
                flag = 0
                flag1 = 0
                if guess_word == "$":
                    continue
                if len(temp) == 0:
                    flag1 = 1
                for pos in range(len(guess_word)):
                    increase_letter_count[ord(guess_word[pos]) - 96] += 1
                    for s in temp:
                        flag1 = 0
                        for t in range(len(guess_word)):
                            if s == guess_word[t]:
                                flag1 = 1
                                break
                        if flag1 == 0:
                            self.words[pos1] = "$"
                            break
                    if flag1 == 0:
                        continue
                    for k in range(len(guess_word)):
                        if self.char[ord(guess_word[k]) - 96] == 0:
                            self.words[pos1] = "$"
                            break
                        elif self.char[ord(guess_word[k]) - 96] == 2:
                            flag = 0
                            for j in range(len(self.index[ord(guess_word[k]) - 96])):
                                if self.index[ord(guess_word[k]) - 96][j] == k:
                                    self.words[pos1] = "$"
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                        elif self.char[ord(guess_word[k]) - 96] == 1:
                            for j in range(len(self.index1[ord(guess_word[k]) - 96])):
                                if self.index1[ord(guess_word[k]) - 96][j] != k:
                                    if (increase_letter_count[ord(guess_word[k]) - 96] > 1 and count_of_similar_letter[ord(guess_word[k]) - 96] != increase_letter_count[ord(guess_word[k]) - 96]):
                                        count_of_similar_letter[ord(guess_word[k]) - 96] += 1
                                    continue
                                self.words[pos1] = "$"
                                flag = 1
                                break
                            else:
                                break
                        if flag == 1:
                            break
                for temp_guess in range(len(self.words)):
                    word1 = self.words[temp_guess]
                    if word1 == "$":
                        continue
                    else:
                        guess = word1
                        self.words[temp_guess] = "$"
                        break
        return guess


game = Game(Solver, N=10)
game.run()
