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
        4,1,14,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,3,0,20,8,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,3,1,29,8,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,63,0,8,1,0,0,0,2,
        23,1,0,0,0,4,39,1,0,0,0,6,51,1,0,0,0,8,9,5,1,0,0,9,10,5,6,0,0,10,
        19,5,2,0,0,11,16,3,2,1,0,12,13,5,2,0,0,13,15,3,2,1,0,14,12,1,0,0,
        0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,20,1,0,0,0,18,16,
        1,0,0,0,19,11,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,3,0,0,
        22,1,1,0,0,0,23,24,5,1,0,0,24,25,5,6,0,0,25,28,5,2,0,0,26,29,3,4,
        2,0,27,29,3,6,3,0,28,26,1,0,0,0,28,27,1,0,0,0,29,34,1,0,0,0,30,31,
        5,2,0,0,31,33,3,2,1,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,
        34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,3,0,0,38,3,1,0,
        0,0,39,40,5,1,0,0,40,41,5,7,0,0,41,42,5,2,0,0,42,43,5,4,0,0,43,44,
        5,2,0,0,44,45,5,5,0,0,45,46,5,2,0,0,46,47,5,7,0,0,47,48,5,2,0,0,
        48,49,5,7,0,0,49,50,5,3,0,0,50,5,1,0,0,0,51,52,5,1,0,0,52,53,5,7,
        0,0,53,54,5,2,0,0,54,55,5,5,0,0,55,56,5,2,0,0,56,57,5,5,0,0,57,58,
        5,2,0,0,58,59,5,7,0,0,59,60,5,2,0,0,60,61,5,7,0,0,61,62,5,3,0,0,
        62,7,1,0,0,0,4,16,19,28,34
    ]

class STFileParser ( Parser ):

    grammarFileName = "STFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "'1'", "'0'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "STRING", "WORD", 
                      "LBRACK", "RBRACK", "SYMBOL", "WS", "COMMENT", "MULTILINE_COMMENT" ]

    RULE_fileStructure = 0
    RULE_entryStructure = 1
    RULE_folderEntry = 2
    RULE_templateEntry = 3

    ruleNames =  [ "fileStructure", "entryStructure", "folderEntry", "templateEntry" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    INT=6
    STRING=7
    WORD=8
    LBRACK=9
    RBRACK=10
    SYMBOL=11
    WS=12
    COMMENT=13
    MULTILINE_COMMENT=14

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

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def entryStructure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STFileParser.EntryStructureContext)
            else:
                return self.getTypedRuleContext(STFileParser.EntryStructureContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(STFileParser.T__0)
            self.state = 9
            self.match(STFileParser.INT)
            self.state = 10
            self.match(STFileParser.T__1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 11
                self.entryStructure()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 12
                    self.match(STFileParser.T__1)
                    self.state = 13
                    self.entryStructure()
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 21
            self.match(STFileParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryStructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def folderEntry(self):
            return self.getTypedRuleContext(STFileParser.FolderEntryContext,0)


        def templateEntry(self):
            return self.getTypedRuleContext(STFileParser.TemplateEntryContext,0)


        def entryStructure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STFileParser.EntryStructureContext)
            else:
                return self.getTypedRuleContext(STFileParser.EntryStructureContext,i)


        def getRuleIndex(self):
            return STFileParser.RULE_entryStructure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntryStructure" ):
                listener.enterEntryStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntryStructure" ):
                listener.exitEntryStructure(self)




    def entryStructure(self):

        localctx = STFileParser.EntryStructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entryStructure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(STFileParser.T__0)
            self.state = 24
            self.match(STFileParser.INT)
            self.state = 25
            self.match(STFileParser.T__1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 26
                self.folderEntry()
                pass

            elif la_ == 2:
                self.state = 27
                self.templateEntry()
                pass


            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 30
                self.match(STFileParser.T__1)
                self.state = 31
                self.entryStructure()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(STFileParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FolderEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

        def getRuleIndex(self):
            return STFileParser.RULE_folderEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFolderEntry" ):
                listener.enterFolderEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFolderEntry" ):
                listener.exitFolderEntry(self)




    def folderEntry(self):

        localctx = STFileParser.FolderEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_folderEntry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(STFileParser.T__0)
            self.state = 40
            self.match(STFileParser.STRING)
            self.state = 41
            self.match(STFileParser.T__1)
            self.state = 42
            self.match(STFileParser.T__3)
            self.state = 43
            self.match(STFileParser.T__1)
            self.state = 44
            self.match(STFileParser.T__4)
            self.state = 45
            self.match(STFileParser.T__1)
            self.state = 46
            self.match(STFileParser.STRING)
            self.state = 47
            self.match(STFileParser.T__1)
            self.state = 48
            self.match(STFileParser.STRING)
            self.state = 49
            self.match(STFileParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

        def getRuleIndex(self):
            return STFileParser.RULE_templateEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateEntry" ):
                listener.enterTemplateEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateEntry" ):
                listener.exitTemplateEntry(self)




    def templateEntry(self):

        localctx = STFileParser.TemplateEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_templateEntry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(STFileParser.T__0)
            self.state = 52
            self.match(STFileParser.STRING)
            self.state = 53
            self.match(STFileParser.T__1)
            self.state = 54
            self.match(STFileParser.T__4)
            self.state = 55
            self.match(STFileParser.T__1)
            self.state = 56
            self.match(STFileParser.T__4)
            self.state = 57
            self.match(STFileParser.T__1)
            self.state = 58
            self.match(STFileParser.STRING)
            self.state = 59
            self.match(STFileParser.T__1)
            self.state = 60
            self.match(STFileParser.STRING)
            self.state = 61
            self.match(STFileParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





