user asks question -> retrieve relevant document chunks -> send chunks + question to LLM -> answer with citations

RECIPE:
use some kind of document parser to collect the content from your pdf 
use some kind of text chunker to break it into smaller pieces 
create a embeddeding model object that gives a numeric value to each chunk based on the meaning of each chunk . Chucks with similar meaning have similar numerical values.
choose a data storage object eg graphs or vector that stores the chucks and their related numerical value. this makes it easier for retrival.