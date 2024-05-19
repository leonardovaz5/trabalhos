while True:
    try:
        n = int(input())  
        input()  
        
        for _ in range(n):
            plants = {}  
            total_plants = 0  
            
            while True:
                try:
                    plant = input().strip()  
                    
                    if not plant: 
                        break
                    
                    if plant in plants:
                        plants[plant] += 1
                    else:
                        plants[plant] = 1
                    total_plants += 1
                except EOFError:  
                    break
            
            if _ > 0:
                print()  
            
            for plant, count in sorted(plants.items()):  
                percentage = (count / total_plants) * 100
                print(f"{plant} {percentage:.4f}")  
    except EOFError:  
        break
