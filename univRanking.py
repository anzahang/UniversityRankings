# Date: November 16, 2022
# CompSci 1026A-003 - Assignment #3
# Name: Andrew Zhang
# This is a program that takes in a country and two csv files, one that has a list of universities(with data of those universities)
# and one that has a list of countries(with information about that country). The program processes the data and completes
# a series of tasks on the data to draw certain conclusions and outputs to a .txt file.

def getInformation(selectedCountry,rankingFileName,capitalsFileName):

    # Checking if the country is USA
    if(selectedCountry != 'USA'):
        # Set the selectedCountry to uppercase
        selectedCountry = selectedCountry.upper()

    # List for final output organization
    data = []
    # List for processed data from ranking csv file
    processedRankings = []
    # Open the ranking csv file with utf-8
    fileContentRankings = open(rankingFileName, "r", encoding='utf8')
    # Iterate through the entire csv line by line while removing format characters and extracting used information
    for line in fileContentRankings:
        results = []
        line = line.strip("\n")
        words = line.split(',')
        results.append(words[0])
        results.append(words[1])
        results.append(words[2])
        results.append(words[3])
        results.append(words[8])
        processedRankings.append(results)
    processedRankings.pop(0)

    # List for processed data from capitals csv file
    processedCapitals = []
    # Open the capitals csv file
    fileContentCapitals = open(capitalsFileName, "r", encoding='utf8')
    # Iterate through the entire csv line by line while removing format characters and extracting used information
    for line in fileContentCapitals:
        results = []
        line = line.strip("\n")
        words = line.split(',')
        results.append(words[0])
        results.append(words[1])
        results.append(words[5])
        processedCapitals.append(results)
    processedCapitals.pop(0)

    # 1.Universities count
    totalUniversities = len(processedRankings)

    # 2.Available Countries
    availableCountries = []
    for university in processedRankings: # Iterate through processed university list
        # Extract countries from data
        if university[2] in availableCountries:
            continue
        else:
            availableCountries.append(university[2])

    # 3.Available Continents
    availableContinents = []
    for capital in processedCapitals: # Iterate through processed capital list
        # Extract continents from data
        if capital[2] in availableContinents:
            continue
        else:
            availableContinents.append(capital[2])

    # 4.University with top international rank
    topUniversityCountry = []
    for university in processedRankings: #Iterate through processed university list
        # Extract the ranking and name of the university for the selected country
        if university[2].upper() == selectedCountry:
            topUniversityCountry.append(university[0])
            topUniversityCountry.append(university[1])
            break
    internationalRank = topUniversityCountry[0]
    universityNameInternational = topUniversityCountry[1]

    # 5.University with top national rank
    nationalRank = ""
    universityNameNational = ""
    for university in processedRankings: # Iterate through processed university list
        # Find the university with the highest national rank for the selected country
        if university[3] == "1" and university[2].upper() == selectedCountry:
            nationalRank = university[3]
            universityNameNational = university[1]
            break

    # 6.Average Score
    sum = 0
    counter = 0
    # Accumulate all the scores of the universities in the selected country
    for university in processedRankings:
        if university[2].upper() == selectedCountry:
            sum+=float(university[4])
            counter+=1
    # Calculate Average
    roundedAverage = float('{0:.1f}'.format(sum/counter))
    average = float(sum/counter)

    # Getting continent
    for continents in processedCapitals:
        if selectedCountry == continents[0].upper():
            continent = continents[2].upper()

    # 7.Relative Score
    scores = []
    countries = []
    # Get all countries in the continent
    for country in processedCapitals:
        if country[2].upper() == continent:
            countries.append(country[0])
    # Get all the scores of the universities in the countries of the continent
    for university in processedRankings:
        if university[2] in countries:
            scores.append(university[4])
    # Find the highest score
    highest = scores[0]
    for score in scores:
        if float(highest) < float(score):
            highest = float(score)
    # Calculate relative score
    relativeScore = (round(average/float(highest),4))*100

    # 8.The capital city
    capital =""
    for country in processedCapitals:
        if country[0].upper() == selectedCountry:
            capital = country[1]

    # 9.The universities that have the capital name in their name
    universities = []
    for university in processedRankings:
        if capital in university[1]:
            universities.append(university[1])

    # Easy access for output
    data.append(totalUniversities)
    data.append(availableCountries)
    data.append(availableContinents)
    data.append(internationalRank)
    data.append(nationalRank)
    data.append(universityNameInternational)
    data.append(universityNameNational)
    data.append(roundedAverage)
    data.append(relativeScore)
    data.append(continent)
    data.append(capital)
    data.append(universities)

    # Output
    f = open("output.txt", "w")
    f.write("Total number of universities => {}\n".format(data[0]))
    f.write("Available countries => {}\n".format(data[1]))
    f.write("Available continents => {}\n".format(data[2]))
    f.write("At international rank => {} the university name is => {}\n".format(data[3], data[5]))
    f.write("At national rank => {} the university name is => {}\n".format(data[4], data[6]))
    f.write("The average score => {}\n".format(data[7]))
    f.write("The relative score to the top university in {} is => ({} / 100.0) x 100% = {}%\n".format(data[9], data[8],data[8]))
    f.write("The capital is => {}\n".format(data[10]))
    f.write("The univerisities that  contain the capital name => \n")
    for i in range(len(data[11])):
        f.write("   #{} {}\n".format(i + 1, data[11][i]))
    f.close()

getInformation("Canada","TopUni.csv","capitals.csv")
