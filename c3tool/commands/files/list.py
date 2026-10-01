"""List one directory."""

from c3tool.commands.files._paths import expand_path
from c3tool.model import BaseCommand, CommandError, CommandSpec, ToolContext

COMMAND_SPEC = CommandSpec("ls", "<filepath, default current>", "Lists a directory.", "python3 script.py ls [filepath]", "Directory entries with type and size.", "c3tool.commands.files.list:ListCommand", order=8)


class ListCommand(BaseCommand):
    def run(self, args, context: ToolContext) -> str:
        # TODO: List either the supplied directory or ``context.cwd``.
        self.require_count(args, 0, "implementation complete")
        target = expand_path(args[0] if args else context.cwd)
        if not target.is_dir():
            raise CommandError(f"{target} is not a valid directory.")
        entries = sorted(target.iterdir())
        if not entries:
            return f"{target} is empty."
        output = []
        for entry in entries:
            if entry.is_dir():
                entry_type = "DIR"
            else:
                entry_type = "FILE"
            size = entry.stat().st_size
            output.append(f"{entry_type} {size:>10} {entry.name}")
        return "\n".join(output)
        # 1. Accept zero or one argument and validate that the target is a folder.
        # 2. Sort entries consistently so output is predictable on every OS.
        # 3. Show a useful type, size, and name for each item.
        # 4. Return a clear message for an empty directory.
        raise NotImplementedError("Implement the ls command")
