import argparse
# Create a parser
parser = argparse.ArgumentParser(description='Meow like a cat.') # Add a description
parser.add_argument("-n", default=1, help="Number of times to meow", type=int) # Add an argument
args = parser.parse_args()  # Parse the arguments

for _ in range(args.n):
    print("meow")

# Run the following command in the terminal
# python flags.py -n 5

# Se a pessoa errar o tipo do argumento, o programa vai dar erro e vai mostrar a mensagem de ajuda.abs

# Or run the following command in the terminal
# python flags.py --help




#pylint: disable-all