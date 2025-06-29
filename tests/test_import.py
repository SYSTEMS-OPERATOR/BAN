import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))


def test_import_hub():
    import hub
    assert hasattr(hub, "main")
