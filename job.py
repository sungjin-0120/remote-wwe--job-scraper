def save_to_file(file_name, pls):
  with open(f"{file_name}.csv","w", encoding="utf8" ) as FIle:
    FIle.write("Company, Title, Location, Pay, Link\n")

    for pl in pls:
      
            
            FIle.write(
                f"{pl['company']},{pl['title']},{pl['location']},{pl['pay']},{pl['link']},\n"
                      ) 
           
