import asyncio
from pii_scanner.scanner import PIIScanner
from pii_scanner.constants.patterns_countries import Regions
import nltk
nltk.download('maxent_ne_chunker_tab')

async def run_scan():
    # Start the timer
    

    pii_scanner = PIIScanner()
    file_path = 'dummy-pii/pan.jpg' 
    

    # data = ['Ankit Gupta', '+919140562125', 'Indian']
    results_list_data = await pii_scanner.scan(file_path=file_path, sample_size=5, region=Regions.IN)
    # results_file_data = await pii_scanner.scan(file_path=file_path, sample_size=0.005, region=Regions.IN)

    print("Results:", results_list_data)

# Run the asynchronous scan
asyncio.run(run_scan())