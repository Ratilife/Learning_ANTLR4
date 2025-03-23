# Generated from STFile.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .STFileParser import STFileParser
else:
    from STFileParser import STFileParser

# This class defines a complete listener for a parse tree produced by STFileParser.
class STFileListener(ParseTreeListener):

    # Enter a parse tree produced by STFileParser#fileStructure.
    def enterFileStructure(self, ctx:STFileParser.FileStructureContext):
        pass

    # Exit a parse tree produced by STFileParser#fileStructure.
    def exitFileStructure(self, ctx:STFileParser.FileStructureContext):
        pass


    # Enter a parse tree produced by STFileParser#rootContent.
    def enterRootContent(self, ctx:STFileParser.RootContentContext):
        pass

    # Exit a parse tree produced by STFileParser#rootContent.
    def exitRootContent(self, ctx:STFileParser.RootContentContext):
        pass


    # Enter a parse tree produced by STFileParser#folderContent.
    def enterFolderContent(self, ctx:STFileParser.FolderContentContext):
        pass

    # Exit a parse tree produced by STFileParser#folderContent.
    def exitFolderContent(self, ctx:STFileParser.FolderContentContext):
        pass


    # Enter a parse tree produced by STFileParser#nestedEntries.
    def enterNestedEntries(self, ctx:STFileParser.NestedEntriesContext):
        pass

    # Exit a parse tree produced by STFileParser#nestedEntries.
    def exitNestedEntries(self, ctx:STFileParser.NestedEntriesContext):
        pass


    # Enter a parse tree produced by STFileParser#entry.
    def enterEntry(self, ctx:STFileParser.EntryContext):
        pass

    # Exit a parse tree produced by STFileParser#entry.
    def exitEntry(self, ctx:STFileParser.EntryContext):
        pass


    # Enter a parse tree produced by STFileParser#headerContent.
    def enterHeaderContent(self, ctx:STFileParser.HeaderContentContext):
        pass

    # Exit a parse tree produced by STFileParser#headerContent.
    def exitHeaderContent(self, ctx:STFileParser.HeaderContentContext):
        pass


    # Enter a parse tree produced by STFileParser#folderHeader.
    def enterFolderHeader(self, ctx:STFileParser.FolderHeaderContext):
        pass

    # Exit a parse tree produced by STFileParser#folderHeader.
    def exitFolderHeader(self, ctx:STFileParser.FolderHeaderContext):
        pass


    # Enter a parse tree produced by STFileParser#forceInt.
    def enterForceInt(self, ctx:STFileParser.ForceIntContext):
        pass

    # Exit a parse tree produced by STFileParser#forceInt.
    def exitForceInt(self, ctx:STFileParser.ForceIntContext):
        pass



del STFileParser