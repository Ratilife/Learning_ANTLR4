# Generated from STFile.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,1,3,1,
        3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,0,0,6,0,2,4,6,8,10,0,0,71,0,12,1,0,0,0,2,18,1,0,0,0,4,40,1,
        0,0,0,6,42,1,0,0,0,8,50,1,0,0,0,10,62,1,0,0,0,12,13,5,7,0,0,13,14,
        5,1,0,0,14,15,5,2,0,0,15,16,3,2,1,0,16,17,5,8,0,0,17,1,1,0,0,0,18,
        23,3,4,2,0,19,20,5,2,0,0,20,22,3,4,2,0,21,19,1,0,0,0,22,25,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,3,1,0,0,0,25,23,1,0,0,0,26,27,5,
        7,0,0,27,28,5,5,0,0,28,29,5,2,0,0,29,30,3,8,4,0,30,31,5,2,0,0,31,
        32,3,6,3,0,32,33,5,8,0,0,33,41,1,0,0,0,34,35,5,7,0,0,35,36,5,3,0,
        0,36,37,5,2,0,0,37,38,3,10,5,0,38,39,5,8,0,0,39,41,1,0,0,0,40,26,
        1,0,0,0,40,34,1,0,0,0,41,5,1,0,0,0,42,47,3,4,2,0,43,44,5,2,0,0,44,
        46,3,4,2,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,
        0,48,7,1,0,0,0,49,47,1,0,0,0,50,51,5,7,0,0,51,52,5,6,0,0,52,53,5,
        2,0,0,53,54,5,1,0,0,54,55,5,2,0,0,55,56,5,5,0,0,56,57,5,2,0,0,57,
        58,5,6,0,0,58,59,5,2,0,0,59,60,5,6,0,0,60,61,5,8,0,0,61,9,1,0,0,
        0,62,63,5,7,0,0,63,64,5,6,0,0,64,65,5,2,0,0,65,66,5,3,0,0,66,67,
        5,2,0,0,67,68,5,5,0,0,68,69,5,2,0,0,69,70,5,6,0,0,70,71,5,2,0,0,
        71,72,5,6,0,0,72,73,5,8,0,0,73,11,1,0,0,0,3,23,40,47
    ]

class STFileParser ( Parser ):

    grammarFileName = "STFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'1'", "','", "'0'", "'\\uFEFF'", "<INVALID>", 
                     "<INVALID>", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOM", "INT", "STRING", "LBRACE", "RBRACE", "WS" ]

    RULE_fileStructure = 0
    RULE_entries = 1
    RULE_entry = 2
    RULE_nested_entries = 3
    RULE_folderHeader = 4
    RULE_templateHeader = 5

    ruleNames =  [ "fileStructure", "entries", "entry", "nested_entries", 
                   "folderHeader", "templateHeader" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    BOM=4
    INT=5
    STRING=6
    LBRACE=7
    RBRACE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileStructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def entries(self):
            return self.getTypedRuleContext(STFileParser.EntriesContext,0)


        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def getRuleIndex(self):
            return STFileParser.RULE_fileStructure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileStructure" ):
                listener.enterFileStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileStructure" ):
                listener.exitFileStructure(self)




    def fileStructure(self):

        localctx = STFileParser.FileStructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_fileStructure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(STFileParser.LBRACE)
            self.state = 13
            self.match(STFileParser.T__0)
            self.state = 14
            self.match(STFileParser.T__1)
            self.state = 15
            self.entries()
            self.state = 16
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntriesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STFileParser.EntryContext)
            else:
                return self.getTypedRuleContext(STFileParser.EntryContext,i)


        def getRuleIndex(self):
            return STFileParser.RULE_entries

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntries" ):
                listener.enterEntries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntries" ):
                listener.exitEntries(self)




    def entries(self):

        localctx = STFileParser.EntriesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entries)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.entry()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 19
                self.match(STFileParser.T__1)
                self.state = 20
                self.entry()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None # Token

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def folderHeader(self):
            return self.getTypedRuleContext(STFileParser.FolderHeaderContext,0)


        def nested_entries(self):
            return self.getTypedRuleContext(STFileParser.Nested_entriesContext,0)


        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def templateHeader(self):
            return self.getTypedRuleContext(STFileParser.TemplateHeaderContext,0)


        def getRuleIndex(self):
            return STFileParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)




    def entry(self):

        localctx = STFileParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entry)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(STFileParser.LBRACE)
                self.state = 27
                localctx.count = self.match(STFileParser.INT)
                self.state = 28
                self.match(STFileParser.T__1)
                self.state = 29
                self.folderHeader()
                self.state = 30
                self.match(STFileParser.T__1)
                self.state = 31
                self.nested_entries()
                self.state = 32
                self.match(STFileParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(STFileParser.LBRACE)
                self.state = 35
                self.match(STFileParser.T__2)
                self.state = 36
                self.match(STFileParser.T__1)
                self.state = 37
                self.templateHeader()
                self.state = 38
                self.match(STFileParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nested_entriesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STFileParser.EntryContext)
            else:
                return self.getTypedRuleContext(STFileParser.EntryContext,i)


        def getRuleIndex(self):
            return STFileParser.RULE_nested_entries

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNested_entries" ):
                listener.enterNested_entries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNested_entries" ):
                listener.exitNested_entries(self)




    def nested_entries(self):

        localctx = STFileParser.Nested_entriesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nested_entries)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.entry()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 43
                self.match(STFileParser.T__1)
                self.state = 44
                self.entry()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FolderHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.flags = None # Token
            self.param1 = None # Token
            self.param2 = None # Token

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def getRuleIndex(self):
            return STFileParser.RULE_folderHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFolderHeader" ):
                listener.enterFolderHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFolderHeader" ):
                listener.exitFolderHeader(self)




    def folderHeader(self):

        localctx = STFileParser.FolderHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_folderHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(STFileParser.LBRACE)
            self.state = 51
            localctx.name = self.match(STFileParser.STRING)
            self.state = 52
            self.match(STFileParser.T__1)
            self.state = 53
            self.match(STFileParser.T__0)
            self.state = 54
            self.match(STFileParser.T__1)
            self.state = 55
            localctx.flags = self.match(STFileParser.INT)
            self.state = 56
            self.match(STFileParser.T__1)
            self.state = 57
            localctx.param1 = self.match(STFileParser.STRING)
            self.state = 58
            self.match(STFileParser.T__1)
            self.state = 59
            localctx.param2 = self.match(STFileParser.STRING)
            self.state = 60
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.flags = None # Token
            self.param1 = None # Token
            self.codeBlock = None # Token

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def getRuleIndex(self):
            return STFileParser.RULE_templateHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateHeader" ):
                listener.enterTemplateHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateHeader" ):
                listener.exitTemplateHeader(self)




    def templateHeader(self):

        localctx = STFileParser.TemplateHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_templateHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(STFileParser.LBRACE)
            self.state = 63
            localctx.name = self.match(STFileParser.STRING)
            self.state = 64
            self.match(STFileParser.T__1)
            self.state = 65
            self.match(STFileParser.T__2)
            self.state = 66
            self.match(STFileParser.T__1)
            self.state = 67
            localctx.flags = self.match(STFileParser.INT)
            self.state = 68
            self.match(STFileParser.T__1)
            self.state = 69
            localctx.param1 = self.match(STFileParser.STRING)
            self.state = 70
            self.match(STFileParser.T__1)
            self.state = 71
            localctx.codeBlock = self.match(STFileParser.STRING)
            self.state = 72
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





