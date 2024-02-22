import pandas as pd
import json
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  # Take a string called "Week" as input
  parser.add_argument('--week', type=str, default='2')
  # Another called "format"
  parser.add_argument('--format', type=str, help='in or pre', default='in')
  # Another called lecchoice
  parser.add_argument('--lecchoice', type=str, help='L1 or L2', default='L2')
  # current csv file
  parser.add_argument('--csvfp', type=str, help='data/attendance_records.csv', default='data/attendance_records.csv')
  args = parser.parse_args()

  # First compile the name for json file. 
  # if format is pre, then it's just L{}-pre.json.format(week) 
  if args.format == 'pre':
    json_file = 'L{}-pre.json'.format(args.week)
  # if format is in, then it's L{}-in-.json.format(week, lecchoice)
  else:
    json_file = 'L{}-in-{}.json'.format(args.week, args.lecchoice)
  
  # Load the json file, fp is under the data folder. 
  with open('data/{}'.format(json_file)) as f:
    data = json.load(f)
  
  # print the length of data['participants'], "The number of participants is:"
  print("The number of participants is: ", len(data['participants']))
  # Get the 'diaplay_name' of all participants
  display_names = [x['display_name'] for x in data['participants']]

  # Load the csv file, fp is under the data folder.
  df = pd.read_csv(args.csvfp)
  # confirm the column name to be updated here. 
  if args.format == 'pre':
    col_name = 'L{}-pre'.format(args.week)
  else:
    col_name = 'L{}-in'.format(args.week)
    
  # Check if the values in the column are all NA, if so, then fill the column with 0.
  if df[col_name].isna().all():
    df[col_name] = 0
  # Loop through the display_names, if the name is in the csv file, then update the column with 1.
  for name in display_names:
    if name in df['name'].values:
      df.loc[df['name'] == name, col_name] = 1
      print("This student has attended {}: {}".format(col_name, name))
  # convert the value in the column to int
  df[col_name] = df[col_name].astype(int)
  # Save the updated csv file.
  df.to_csv(args.csvfp, index=False)

  # print where the csv file is saved.
  print("The csv file is saved at: ", args.csvfp)