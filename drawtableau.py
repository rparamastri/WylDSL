import argparse
import semantics, parser, tree_structure

def main():
    """
    Takes in arguments and calls the draw function.
    """
    argparser = argparse.ArgumentParser()

    argparser.add_argument("filename", help="the file containing your code")

    argparser.add_argument("-f", "--format", help="format of the image file "
                                               "('pdf', 'png', etc.)",
                           default='png')
    argparser.add_argument("-o", "--out", help="the name of the image file",
                           default='out')
    argparser.add_argument("-d", "--dot", help="produce the DOT code as well",
                           action="store_true")
    
    args = argparser.parse_args()

    # read the file containing the code
    f = open(args.filename, 'r') 
    user_code = f.read()
    f.close()

    # get the structure of the tree
    node_list = parser.parser.parse(user_code)
    tree      = tree_structure.Tree(node_list)
    
    semantics.draw(tree, args.format, args.out, args.dot)
    print("Drew to {}.{}".format(args.out, args.format))

if __name__ == '__main__':
    main()

