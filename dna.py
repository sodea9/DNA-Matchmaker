import csv
import sys

def read_dna(dna_filename):
   """
   Input: file name
   Process: reads from file
   Returns: dna sequence as string
   """
   with open(dna_filename, 'r') as f:
      sequence = f.read()
   return sequence

def dna_length(dna_filename):
   """
   Input: file name
   Process: reads from file
   Returns: length of dna sequence
   """
   with open(dna_filename, 'r') as f:
      sequence = f.read()
   return len(sequence)

def read_strs(str_filename):
   """
   Input: csv file containing each person's profile
   Process: reads from file
   Returns: list of dictionaries, each being a profile
   """
   with open(str_filename, 'r') as f:
      csv_file = csv.DictReader(f)
      profiles = []
      for item in csv_file:
         profiles.append(item)
   return profiles
 
 
def get_strs(str_profile):
   """
   Input: singular person's profile in dictionary format
   Process: unpacks keys and values into a list of tuples
   Returns: said list of tuples (without the person's name though)
   """
   pairs = [] #list to add tuple pairs to
   for key in str_profile:
      #omits first key index(name) from tuple list
      if key == 'name':
         continue
      pairs.append(tuple((key, int(str_profile[key])))) #converts each pair to a tuple and appends onto list
   return pairs

def longest_str_repeat_count(str_frag, dna_seq):
   """
   Input: 4 letter DNA fragment, whole DNA sequence
   Process: counts the longest repeated sequence of the
   given fragment in the DNA strand
   Returns: maximum number of times repeated in a row
   """
   i = 0
   timesRepeated = 0
   maxRepeat = 0
   while i <= len(dna_seq)-4:
      if dna_seq[i:i+4] == str_frag:
        timesRepeated += 1
        i += 4
      else:
         if timesRepeated > maxRepeat:
            maxRepeat = timesRepeated
         timesRepeated = 0
         i += 1
   if timesRepeated > maxRepeat:
      return timesRepeated
   return maxRepeat

def find_match(str_profile, dna_seq):
   """
   Input: singular profile(list of tuples), DNA sequence
   Process: checks if DNA strand matches profile that was given
   Returns: True if it's a match, False otherwise
   """
   matches = 0
   for tuple in str_profile:
      if longest_str_repeat_count(tuple[0], dna_seq) == tuple[1]:
         matches += 1
   return matches == 3

def dna_match(str_filename, dna_filename):
   """
   Input: csv profile file name, cna sequence file name
   Process: uses all of the previous functions to determine the match and finds name
   Returns: string of matched name or 'no match'
   """
   dnaSequence = read_dna(dna_filename)
   profiles = read_strs(str_filename)
   for person in profiles:
      if find_match(get_strs(person), dnaSequence):
         return person['name']
   return "No match"
   
if __name__ == '__main__':
   if len(sys.argv) != 3:   #checks if proper amount of arguments
      print('Usage: python dna.py STR_FILE DNA_FILE')
      quit()
   print(dna_match(sys.argv[1], sys.argv[2])) #uses file names as params of matching function