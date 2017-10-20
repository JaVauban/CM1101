python -m doctest -v ./game2/game.py 
set /p DUMMY=Press ENTER to test gameparser
python -m doctest -v ./game2/gameparser.py
set /p DUMMY=Press ENTER to run game
python ./game2/game.py