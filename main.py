from regex import *
import wordSpilitter
import SyntaxAnalyzer
import SemanticAnalyzer


Tokens = wordSpilitter.wordCount("words.txt")
# print(Tokens)

SemanticAnalyzer.Semantic_Analyzer(Tokens)
#SyntaxAnalyzer.Syntax_Analyzer(Tokens)