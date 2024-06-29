
def generateBoard(self, difficulty=None):
    # http://norvig.com/sudoku.html
    # If a contradiction is reached, start over.
    # If we fill at least 17 squares with at least 8 different digits then we are done.
    # (Note: with less than 17 squares filled in or less than 8 different digits it is known that there will be duplicate solutions.
    #successfulBoardGeneration = False
    minimumDigitPlacement = 30
    minimumUniqueDigits = 8

    placedDigitsCount = 0
    uniquePlacedDigits=[]
    while(not (placedDigitsCount >= minimumDigitPlacement and len(uniquePlacedDigits) >= minimumUniqueDigits)):

        # Random Position
        positionPlacement = int(self.getRandomUnsolvedBoardPosition())
        potentialGuesses = self.getPotentialGuesses(boardIndex=positionPlacement)
        print('At position ' + str(positionPlacement) + ' I can possibly place these guesses:' + str(potentialGuesses))
        '''
        if(len(potentialGuesses) < 1):
            print('Darnit! I cant place anything at position ' + str(positionPlacement) + '. This puzzle must be invalid:\n' + str(self))

            # Start over!
            placedDigitsCount = 0
            uniquePlacedDigits = []
            self.board = [0]*81
        
        else:
        '''
        currentGuess = int(list(potentialGuesses)[random.randint(0,len(potentialGuesses)-1)])

        print('I will place a ' + str(currentGuess) + ' at position ' + str(positionPlacement))
        self.board[positionPlacement] = currentGuess
        if(self.isValid()):
            print('This board is still valid.')
            uniquePlacedDigits.append(currentGuess)
            uniquePlacedDigits = list(set(uniquePlacedDigits))
            placedDigitsCount += 1
        else:
            print('Darnit! Placing a ' + str(currentGuess) + ' at ' + str(positionPlacement) + 'made puzzle must be invalid, starting over:\n' + str(self))
            placedDigitsCount = 0
            uniquePlacedDigits = []
            self.board = [0]*81

    print('Done. I have placed ' + str(placedDigitsCount) + ' digits, ' + str(len(uniquePlacedDigits)) + ' unique.')

