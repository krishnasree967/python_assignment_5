# # Slice list into 3 equal chunks and reverse each chunk.

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunks = len(sample_list)// 3

current_chunk = []

for j, num in enumerate(sample_list):
    current_chunk.append(num)
    
    if len(current_chunk) == chunks or j== len(sample_list) - 1:
    
        print(f"Chunk {j // chunks + 1} {current_chunk}")
        
        reversed_chunk = current_chunk[::-1]
        print(f"After reversing {reversed_chunk}\n")
        
        current_chunk = []