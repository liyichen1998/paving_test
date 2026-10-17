import subprocess,sys,unittest
from pathlib import Path

class LegacyPeriodicWitness(unittest.TestCase):
    def test_eight_base_periodic_witness_reproduces(self):
        p=Path(__file__).parents[1]/"legacy"/"test_eight_base_periodic_tiling.py"
        r=subprocess.run([sys.executable,str(p)],capture_output=True,text=True,timeout=20)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIn("FOUND",r.stdout)
        self.assertIn("2 2 FOUND",r.stdout)

if __name__=="__main__":
    unittest.main()
