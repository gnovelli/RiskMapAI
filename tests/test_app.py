from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
import app

def test_main_runs_without_error():
    app.main()
