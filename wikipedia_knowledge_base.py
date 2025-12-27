#Importing the wikipedia library 
import wikipedia
def curate_date(data_list):
    curated_results = {}
    for item in data_list:
        try:
            #Get the page title for the search term 
            page = wikipedia.page(item)
            curated_results[item] = page.url
            print(f"Linked: {item} -> {page.url}")
        except:
            #Handled cases where Wikipedia is confused or the item isn't found
            curated_results[item] = "No Wikipedia link is found"
    return curated_results
#Your "Dataset"
my_data = ["Ebenezer Scrooge", "Machine Learning", "Git Bash"]
link = curate_data(my_data)
 
