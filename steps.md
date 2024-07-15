# ingest pipeline redesign steps

- modify utils.prepare_data.prepare_data to return clean df without splitting
- ingest block returns 1 df, cleaned by utils.prepare_data.prepare_data
- delete global data product

- in prepare pipeline: modify ingest block with code from ingest_new
- in prepare pipeline: add dynamic data transform block called split after that splits the data into train validation
- in prepare pipeline: add data transform block prepare, with code from prepare_test (use prepare_new if that doesn't work)
- in prepare pipeline: add data export build that saves the the data as a csv file - code in build_new 
- in train pipeline: replace gdp block with data loader that reads from data/train and data/val
- in train pipeline: in data loader, train + fit dict vectorizer
- in train pipeline: modify train block to read train + val data from data loader
- in test pipeline: start with data loader that reads from data/test
- in test pipeline: in data loader, open dv and fit it on test data

- instead of:
ingest -> prepare -> build
- use
ingest -> split (dynamic) -> prepare -> build

test pipeline:
ingest -> prepare -> build


# data directory structure

data/  
data/train  
data/val  
data/test  
data/archive  
data/archive/train  
data/archive/val  
data/archive/test  

# training cycle

- read input data from data/test folder + rename file in data/test "input_data_{date}.csv"
- split data into training + validation test set
- save training set into data/train + rename file in data/train "train_data_{datetime}.csv"
- save validation set inot data/val + rename file in data/val "val_data_{datetime}.csv"

# test cycle

- download new file into data/test (using a streamlit download button)
- ingest new file from data/test using ingest block used for training
- 
