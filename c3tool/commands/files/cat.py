"""Print a text file."""

from c3tool.commands.files._paths import require_existing_file
from c3tool.model import BaseCommand, CommandSpec, ToolContext

COMMAND_SPEC = CommandSpec("cat", "<filepath>", "Prints a text file.", "python3 script.py cat <filepath>", "The complete file contents.", "c3tool.commands.files.cat:CatCommand", order=3)


class CatCommand(BaseCommand):
    def run(self, args, context: ToolContext) -> str:
        # TODO: Read and return one text file.
        self.require_range(args, 1, 1, "implementation complete")
        filepath = require_existing_file(args[0], context)
        return filepath.read_text(encoding="utf-8")
        # 1. Require exactly one filepath.
        # 2. Use ``require_existing_file`` for a friendly missing-file error.
        # 3. Read as UTF-8; decide how invalid bytes should be handled.
        raise NotImplementedError("Implement the cat command")
