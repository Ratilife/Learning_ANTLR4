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
        4,1,9,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,
        30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,5,4,54,8,4,10,4,12,4,57,9,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,
        1,0,2,3,78,0,14,1,0,0,0,2,20,1,0,0,0,4,26,1,0,0,0,6,48,1,0,0,0,8,
        50,1,0,0,0,10,58,1,0,0,0,12,70,1,0,0,0,14,15,5,7,0,0,15,16,5,5,0,
        0,16,17,5,1,0,0,17,18,3,2,1,0,18,19,5,8,0,0,19,1,1,0,0,0,20,21,5,
        7,0,0,21,22,5,5,0,0,22,23,5,1,0,0,23,24,3,4,2,0,24,25,5,8,0,0,25,
        3,1,0,0,0,26,31,3,10,5,0,27,28,5,1,0,0,28,30,3,6,3,0,29,27,1,0,0,
        0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,5,1,0,0,0,33,31,1,
        0,0,0,34,35,5,7,0,0,35,36,5,5,0,0,36,37,5,1,0,0,37,38,3,10,5,0,38,
        39,5,1,0,0,39,40,3,8,4,0,40,41,5,8,0,0,41,49,1,0,0,0,42,43,5,7,0,
        0,43,44,5,2,0,0,44,45,5,1,0,0,45,46,3,12,6,0,46,47,5,8,0,0,47,49,
        1,0,0,0,48,34,1,0,0,0,48,42,1,0,0,0,49,7,1,0,0,0,50,55,3,6,3,0,51,
        52,5,1,0,0,52,54,3,6,3,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,
        0,55,56,1,0,0,0,56,9,1,0,0,0,57,55,1,0,0,0,58,59,5,7,0,0,59,60,5,
        6,0,0,60,61,5,1,0,0,61,62,5,5,0,0,62,63,5,1,0,0,63,64,5,5,0,0,64,
        65,5,1,0,0,65,66,5,6,0,0,66,67,5,1,0,0,67,68,5,6,0,0,68,69,5,8,0,
        0,69,11,1,0,0,0,70,71,5,7,0,0,71,72,5,6,0,0,72,73,5,1,0,0,73,74,
        5,2,0,0,74,75,5,1,0,0,75,76,7,0,0,0,76,77,5,1,0,0,77,78,5,6,0,0,
        78,79,5,1,0,0,79,80,5,6,0,0,80,81,5,8,0,0,81,13,1,0,0,0,3,31,48,
        55
    ]

class STFileParser ( Parser ):

    grammarFileName = "STFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'0'", "'1'", "'\\uFEFF'", "<INVALID>", 
                     "<INVALID>", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOM", "INT", "STRING", "LBRACE", "RBRACE", "WS" ]

    RULE_fileStructure = 0
    RULE_rootContent = 1
    RULE_folderContent = 2
    RULE_entry = 3
    RULE_entryList = 4
    RULE_folderHeader = 5
    RULE_templateHeader = 6

    ruleNames =  [ "fileStructure", "rootContent", "folderContent", "entry", 
                   "entryList", "folderHeader", "templateHeader" ]

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

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def rootContent(self):
            return self.getTypedRuleContext(STFileParser.RootContentContext,0)


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
            self.state = 14
            self.match(STFileParser.LBRACE)
            self.state = 15
            self.match(STFileParser.INT)
            self.state = 16
            self.match(STFileParser.T__0)
            self.state = 17
            self.rootContent()
            self.state = 18
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def folderContent(self):
            return self.getTypedRuleContext(STFileParser.FolderContentContext,0)


        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def getRuleIndex(self):
            return STFileParser.RULE_rootContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootContent" ):
                listener.enterRootContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootContent" ):
                listener.exitRootContent(self)




    def rootContent(self):

        localctx = STFileParser.RootContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rootContent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(STFileParser.LBRACE)
            self.state = 21
            self.match(STFileParser.INT)
            self.state = 22
            self.match(STFileParser.T__0)
            self.state = 23
            self.folderContent()
            self.state = 24
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FolderContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def folderHeader(self):
            return self.getTypedRuleContext(STFileParser.FolderHeaderContext,0)


        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STFileParser.EntryContext)
            else:
                return self.getTypedRuleContext(STFileParser.EntryContext,i)


        def getRuleIndex(self):
            return STFileParser.RULE_folderContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFolderContent" ):
                listener.enterFolderContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFolderContent" ):
                listener.exitFolderContent(self)




    def folderContent(self):

        localctx = STFileParser.FolderContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_folderContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.folderHeader()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 27
                self.match(STFileParser.T__0)
                self.state = 28
                self.entry()
                self.state = 33
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

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def folderHeader(self):
            return self.getTypedRuleContext(STFileParser.FolderHeaderContext,0)


        def entryList(self):
            return self.getTypedRuleContext(STFileParser.EntryListContext,0)


        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

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
        self.enterRule(localctx, 6, self.RULE_entry)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(STFileParser.LBRACE)
                self.state = 35
                self.match(STFileParser.INT)
                self.state = 36
                self.match(STFileParser.T__0)
                self.state = 37
                self.folderHeader()
                self.state = 38
                self.match(STFileParser.T__0)
                self.state = 39
                self.entryList()
                self.state = 40
                self.match(STFileParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(STFileParser.LBRACE)
                self.state = 43
                self.match(STFileParser.T__1)
                self.state = 44
                self.match(STFileParser.T__0)
                self.state = 45
                self.templateHeader()
                self.state = 46
                self.match(STFileParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryListContext(ParserRuleContext):
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
            return STFileParser.RULE_entryList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntryList" ):
                listener.enterEntryList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntryList" ):
                listener.exitEntryList(self)




    def entryList(self):

        localctx = STFileParser.EntryListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_entryList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.entry()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 51
                self.match(STFileParser.T__0)
                self.state = 52
                self.entry()
                self.state = 57
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

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.INT)
            else:
                return self.getToken(STFileParser.INT, i)

        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

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
        self.enterRule(localctx, 10, self.RULE_folderHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(STFileParser.LBRACE)
            self.state = 59
            self.match(STFileParser.STRING)
            self.state = 60
            self.match(STFileParser.T__0)
            self.state = 61
            self.match(STFileParser.INT)
            self.state = 62
            self.match(STFileParser.T__0)
            self.state = 63
            self.match(STFileParser.INT)
            self.state = 64
            self.match(STFileParser.T__0)
            self.state = 65
            self.match(STFileParser.STRING)
            self.state = 66
            self.match(STFileParser.T__0)
            self.state = 67
            self.match(STFileParser.STRING)
            self.state = 68
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

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

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
        self.enterRule(localctx, 12, self.RULE_templateHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(STFileParser.LBRACE)
            self.state = 71
            self.match(STFileParser.STRING)
            self.state = 72
            self.match(STFileParser.T__0)
            self.state = 73
            self.match(STFileParser.T__1)
            self.state = 74
            self.match(STFileParser.T__0)
            self.state = 75
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            self.match(STFileParser.T__0)
            self.state = 77
            self.match(STFileParser.STRING)
            self.state = 78
            self.match(STFileParser.T__0)
            self.state = 79
            self.match(STFileParser.STRING)
            self.state = 80
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





