#------------------------------------------------------------------------
#description : Match groups
#Used to search for partictular pattern
#------------------------------------------------------------------------
import re

match =re.search('(\d{3}) (\d{2})','39801 356 222 101' );
if(match):
  print("Match Group Index 1 position "+match.group(1));
  print("Match Group Index 2 position "+match.group(2));
  print(match.groups());
  print(match.span());
  print(match.start());
  print(match.end());
else:
  print("Match Not Found");
