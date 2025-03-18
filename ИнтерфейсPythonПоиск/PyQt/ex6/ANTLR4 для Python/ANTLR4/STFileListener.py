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


    # Enter a parse tree produced by STFileParser#entries.
    def enterEntries(self, ctx:STFileParser.EntriesContext):
        pass

    # Exit a parse tree produced by STFileParser#entries.
    def exitEntries(self, ctx:STFileParser.EntriesContext):
        pass


    # Enter a parse tree produced by STFileParser#entry.
    def enterEntry(self, ctx:STFileParser.EntryContext):
        pass

    # Exit a parse tree produced by STFileParser#entry.
    def exitEntry(self, ctx:STFileParser.EntryContext):
        pass


    # Enter a parse tree produced by STFileParser#nested_entries.
    def enterNested_entries(self, ctx:STFileParser.Nested_entriesContext):
        pass

    # Exit a parse tree produced by STFileParser#nested_entries.
    def exitNested_entries(self, ctx:STFileParser.Nested_entriesContext):
        pass


    # Enter a parse tree produced by STFileParser#folderHeader.
    def enterFolderHeader(self, ctx:STFileParser.FolderHeaderContext):
        pass

    # Exit a parse tree produced by STFileParser#folderHeader.
    def exitFolderHeader(self, ctx:STFileParser.FolderHeaderContext):
        pass


    # Enter a parse tree produced by STFileParser#templateHeader.
    def enterTemplateHeader(self, ctx:STFileParser.TemplateHeaderContext):
        pass

    # Exit a parse tree produced by STFileParser#templateHeader.
    def exitTemplateHeader(self, ctx:STFileParser.TemplateHeaderContext):
        pass



del STFileParser