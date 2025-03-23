# Generated from STFile.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from STFileParserExtensions import STFileParserExtensions
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,57,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,
        10,12,14,0,0,80,0,16,1,0,0,0,2,22,1,0,0,0,4,28,1,0,0,0,6,32,1,0,
        0,0,8,56,1,0,0,0,10,58,1,0,0,0,12,71,1,0,0,0,14,83,1,0,0,0,16,17,
        5,9,0,0,17,18,5,1,0,0,18,19,5,2,0,0,19,20,3,2,1,0,20,21,5,10,0,0,
        21,1,1,0,0,0,22,23,5,9,0,0,23,24,3,14,7,0,24,25,5,2,0,0,25,26,3,
        4,2,0,26,27,5,10,0,0,27,3,1,0,0,0,28,29,3,12,6,0,29,30,5,2,0,0,30,
        31,3,6,3,0,31,5,1,0,0,0,32,37,3,8,4,0,33,34,5,2,0,0,34,36,3,8,4,
        0,35,33,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,7,1,
        0,0,0,39,37,1,0,0,0,40,41,5,9,0,0,41,42,3,14,7,0,42,43,5,2,0,0,43,
        44,3,10,5,0,44,45,5,2,0,0,45,46,3,6,3,0,46,47,5,10,0,0,47,48,4,4,
        0,1,48,57,1,0,0,0,49,50,5,9,0,0,50,51,5,3,0,0,51,52,5,2,0,0,52,53,
        3,10,5,0,53,54,5,10,0,0,54,55,4,4,1,1,55,57,1,0,0,0,56,40,1,0,0,
        0,56,49,1,0,0,0,57,9,1,0,0,0,58,59,5,9,0,0,59,60,5,7,0,0,60,61,5,
        2,0,0,61,62,5,6,0,0,62,63,5,2,0,0,63,64,5,6,0,0,64,65,5,2,0,0,65,
        66,5,7,0,0,66,67,5,2,0,0,67,68,5,7,0,0,68,69,5,10,0,0,69,70,6,5,
        -1,0,70,11,1,0,0,0,71,72,5,9,0,0,72,73,5,7,0,0,73,74,5,2,0,0,74,
        75,5,1,0,0,75,76,5,2,0,0,76,77,5,3,0,0,77,78,5,2,0,0,78,79,5,7,0,
        0,79,80,5,2,0,0,80,81,5,7,0,0,81,82,5,10,0,0,82,13,1,0,0,0,83,84,
        4,7,2,0,84,85,5,6,0,0,85,15,1,0,0,0,2,37,56
    ]

class STFileParser ( Parser ):

    grammarFileName = "STFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'1'", "','", "'0'", "'\\uFEFF'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOM", "WORD", "INT", "STRING", "SYMBOL", "LBRACE", 
                      "RBRACE", "WS" ]

    RULE_fileStructure = 0
    RULE_rootContent = 1
    RULE_folderContent = 2
    RULE_nestedEntries = 3
    RULE_entry = 4
    RULE_headerContent = 5
    RULE_folderHeader = 6
    RULE_forceInt = 7

    ruleNames =  [ "fileStructure", "rootContent", "folderContent", "nestedEntries", 
                   "entry", "headerContent", "folderHeader", "forceInt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    BOM=4
    WORD=5
    INT=6
    STRING=7
    SYMBOL=8
    LBRACE=9
    RBRACE=10
    WS=11

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
            self.state = 16
            self.match(STFileParser.LBRACE)
            self.state = 17
            self.match(STFileParser.T__0)
            self.state = 18
            self.match(STFileParser.T__1)
            self.state = 19
            self.rootContent()
            self.state = 20
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
            self.count = None # ForceIntContext

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def folderContent(self):
            return self.getTypedRuleContext(STFileParser.FolderContentContext,0)


        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def forceInt(self):
            return self.getTypedRuleContext(STFileParser.ForceIntContext,0)


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
            self.state = 22
            self.match(STFileParser.LBRACE)
            self.state = 23
            localctx.count = self.forceInt()
            self.state = 24
            self.match(STFileParser.T__1)
            self.state = 25
            self.folderContent()
            self.state = 26
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


        def nestedEntries(self):
            return self.getTypedRuleContext(STFileParser.NestedEntriesContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.folderHeader()
            self.state = 29
            self.match(STFileParser.T__1)
            self.state = 30
            self.nestedEntries()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NestedEntriesContext(ParserRuleContext):
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
            return STFileParser.RULE_nestedEntries

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedEntries" ):
                listener.enterNestedEntries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedEntries" ):
                listener.exitNestedEntries(self)




    def nestedEntries(self):

        localctx = STFileParser.NestedEntriesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nestedEntries)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.entry()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 33
                self.match(STFileParser.T__1)
                self.state = 34
                self.entry()
                self.state = 39
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
            self.count = None # ForceIntContext
            self.header = None # HeaderContentContext

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def nestedEntries(self):
            return self.getTypedRuleContext(STFileParser.NestedEntriesContext,0)


        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def forceInt(self):
            return self.getTypedRuleContext(STFileParser.ForceIntContext,0)


        def headerContent(self):
            return self.getTypedRuleContext(STFileParser.HeaderContentContext,0)


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
        self.enterRule(localctx, 8, self.RULE_entry)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(STFileParser.LBRACE)
                self.state = 41
                localctx.count = self.forceInt()
                self.state = 42
                self.match(STFileParser.T__1)
                self.state = 43
                localctx.header = self.headerContent()
                self.state = 44
                self.match(STFileParser.T__1)
                self.state = 45
                self.nestedEntries()
                self.state = 46
                self.match(STFileParser.RBRACE)
                self.state = 47
                if not STFileParserExtensions.isFolder(localctx.header.type_, localctx.header.flags):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "STFileParserExtensions.isFolder($header.type, $header.flags)")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(STFileParser.LBRACE)
                self.state = 50
                self.match(STFileParser.T__2)
                self.state = 51
                self.match(STFileParser.T__1)
                self.state = 52
                localctx.header = self.headerContent()
                self.state = 53
                self.match(STFileParser.RBRACE)
                self.state = 54
                if not STFileParserExtensions.isTemplate(localctx.header.type_, localctx.header.flags):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "STFileParserExtensions.isTemplate($header.type, $header.flags)")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.flags = None
            self.name = None # Token
            self.t_type = None # Token
            self.f_flags = None # Token
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

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.INT)
            else:
                return self.getToken(STFileParser.INT, i)

        def getRuleIndex(self):
            return STFileParser.RULE_headerContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderContent" ):
                listener.enterHeaderContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderContent" ):
                listener.exitHeaderContent(self)




    def headerContent(self):

        localctx = STFileParser.HeaderContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_headerContent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(STFileParser.LBRACE)
            self.state = 59
            localctx.name = self.match(STFileParser.STRING)
            self.state = 60
            self.match(STFileParser.T__1)
            self.state = 61
            localctx.t_type = self.match(STFileParser.INT)
            self.state = 62
            self.match(STFileParser.T__1)
            self.state = 63
            localctx.f_flags = self.match(STFileParser.INT)
            self.state = 64
            self.match(STFileParser.T__1)
            self.state = 65
            localctx.param1 = self.match(STFileParser.STRING)
            self.state = 66
            self.match(STFileParser.T__1)
            self.state = 67
            localctx.param2 = self.match(STFileParser.STRING)
            self.state = 68
            self.match(STFileParser.RBRACE)

            # Присваиваем возвращаемые значения
            localctx.type_ =  (None if localctx.t_type is None else localctx.t_type.text)
            localctx.flags =  (None if localctx.f_flags is None else localctx.f_flags.text)
                
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
            self.empty1 = None # Token
            self.empty2 = None # Token

        def LBRACE(self):
            return self.getToken(STFileParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(STFileParser.RBRACE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(STFileParser.STRING)
            else:
                return self.getToken(STFileParser.STRING, i)

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
        self.enterRule(localctx, 12, self.RULE_folderHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(STFileParser.LBRACE)
            self.state = 72
            localctx.name = self.match(STFileParser.STRING)
            self.state = 73
            self.match(STFileParser.T__1)
            self.state = 74
            self.match(STFileParser.T__0)
            self.state = 75
            self.match(STFileParser.T__1)
            self.state = 76
            self.match(STFileParser.T__2)
            self.state = 77
            self.match(STFileParser.T__1)
            self.state = 78
            localctx.empty1 = self.match(STFileParser.STRING)
            self.state = 79
            self.match(STFileParser.T__1)
            self.state = 80
            localctx.empty2 = self.match(STFileParser.STRING)
            self.state = 81
            self.match(STFileParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForceIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(STFileParser.INT, 0)

        def getRuleIndex(self):
            return STFileParser.RULE_forceInt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForceInt" ):
                listener.enterForceInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForceInt" ):
                listener.exitForceInt(self)




    def forceInt(self):

        localctx = STFileParser.ForceIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forceInt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            if not STFileParserExtensions.isInteger(_input.LT(1).text):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "STFileParserExtensions.isInteger(_input.LT(1).text)")
            self.state = 84
            self.match(STFileParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.entry_sempred
        self._predicates[7] = self.forceInt_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def entry_sempred(self, localctx:EntryContext, predIndex:int):
            if predIndex == 0:
                return STFileParserExtensions.isFolder(localctx.header.type_, localctx.header.flags)
         

            if predIndex == 1:
                return STFileParserExtensions.isTemplate(localctx.header.type_, localctx.header.flags)
         

    def forceInt_sempred(self, localctx:ForceIntContext, predIndex:int):
            if predIndex == 2:
                return STFileParserExtensions.isInteger(_input.LT(1).text)
         




