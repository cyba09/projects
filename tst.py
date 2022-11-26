from tqdm import tqdm
from time import sleep

pbar = tqdm(total=100)
pbar.set_description("Processing")
pbar.update(200)
pbar.close()

