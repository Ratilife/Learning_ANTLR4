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


    # Enter a parse tree produced by STFileParser#entryStructure.
    def enterEntryStructure(self, ctx:STFileParser.EntryStructureContext):
        pass

    # Exit a parse tree produced by STFileParser#entryStructure.
    def exitEntryStructure(self, ctx:STFileParser.EntryStructureContext):
        pass


    # Enter a parse tree produced by STFileParser#folderEntry.
    def enterFolderEntry(self, ctx:STFileParser.FolderEntryContext):
        pass

    # Exit a parse tree produced by STFileParser#folderEntry.
    def exitFolderEntry(self, ctx:STFileParser.FolderEntryContext):
        pass


    # Enter a parse tree produced by STFileParser#templateEntry.
    def enterTemplateEntry(self, ctx:STFileParser.TemplateEntryContext):
        pass

    # Exit a parse tree produced by STFileParser#templateEntry.
    def exitTemplateEntry(self, ctx:STFileParser.TemplateEntryContext):
        pass



del STFileParser