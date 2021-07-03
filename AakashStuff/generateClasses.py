import csv

keywords = ["bottle", "plastic", "paper", "apple", "mango", "banana", "cherry", "berry", "food", "trash", "waste"]


def loadClasses():
    signs = []
    with open('class-descriptions.csv', 'r', encoding="utf8") as csvfile:
        signnames = csv.reader(csvfile, delimiter=',')
        for row in signnames:
            signs.append(row[1])
        csvfile.close()
    classesToUse = []
    for item in signs:
        for keyword in keywords:
            if keyword in item.lower():
                print(item)
                classesToUse.append(item)
    out = "python main.py downloader --classes "
    for c in classesToUse:
        out += f"\"{c}\" "
    out += "--type_csv train --limit 8000"
    print(out)


loadClasses()
# python main.py downloader --classes 'Water bottle' 'Brazilian food' 'Lingonberry' 'Banana family' 'Apple' 'Apple pie' 'Food coloring' 'Mulberry' 'Dewberry' 'Gooseberry' 'Boysenberry' 'Nannyberry' 'Fast food' 'Elderberry' 'Cloudberry' 'Bilberry' 'Photographic paper' 'Waste' 'Baby bottle' 'Wax paper' 'Andhra food' 'Local food' 'Dog food' 'Wallpaper' 'Raspberry' 'Food storage' 'Asian food' 'Bottlenose dolphin' 'Scrapple' 'Malaysian food' 'Cantonese food' 'Cajun food' 'Purple mangosteen' 'Take-out food' 'Cherry blossom' 'Paper bag' 'Chinese food' 'Frozen food' 'Caribbean food' 'American food' 'Southeast asian food' 'Kosher food' 'Cranberry' 'Wine bottle' 'Convenience food' 'Staple food' 'Bottled water' 'Indonesian food' 'Rice paper' 'Nissan cherry' 'Cherry pie' 'Salmonberry' 'Apple beer' 'Banana leaf' 'Polish food' 'Hollyleaf cherry' 'Blackberry lily' 'Fire cherry' 'Paperwhite' 'Plastic arts' 'Bottle cap' 'Apple juice' 'Cuban food' 'À la carte food' 'Latin american food' 'European food' 'Food poisoning' 'Newspaper delivery' 'Ethiopian food' 'Apple cider' 'Bottlenose whales' 'Strawberry guava' 'Pet food' 'Sour cherry soup' 'Joss paper' 'Paper wrapped cake' 'Sugar-apple' 'Custard-apple' 'Applejack' 'Festival foods' 'Origami paper' 'Wild crabapple' 'Plastic bottle' 'Plastic bottle' 'Jamaican food' 'Food processing' 'Wheatberry' 'Seafood birdsnest' 'Paper towel' 'Food' 'Fizzy apple cocktail' 'Preserved food' 'French food' 'Russian food' 'Silver buffaloberry' 'White mulberry' 'Olallieberry' 'Chokeberry' 'Saimin food' 'Food additive' 'Loganberry' 'Chokecherry' 'German food' 'Greek food' 'Fast food restaurant' 'Pineapple lumps' 'Food dehydrator' 'Cambodian food' 'Wash bottle' 'Churrasco food' 'Swiss food' 'Huckleberry' 'Baby food' 'Eastern european food' 'Wine raspberry' 'Middle eastern food' 'Food steamer' 'Guavaberry' 'Irish food' 'Portuguese food' 'Animal source foods' 'Food court' 'Computer wallpaper' 'Banana roll' 'Paper lantern' 'Food processor' 'Cranberry juice' 'Raspberry vinegar' 'Beer bottle' 'Ilex verticillataAmerican Winterberry' 'West Indian raspberry ' 'Crabapple' 'Candy apple' 'Korean food' 'Cat food' 'Sandpaper fig' 'Banana bread' 'Native gooseberry' 'Native raspberry' 'Runza food' 'Bottle' 'Cedar bay cherry' 'Bottle opener' 'Apple strudel' 'Superfood' 'Bottlebush' 'Hackberry Emperor' 'Star apple' 'Comfort food' 'Peruvian groundcherry' 'Food truck' 'Mediterranean food' 'Southwestern united states food' 'Apple mint' 'Mexican food' 'Apple cider vinegar' 'Hawaiian food' 'Apple crisp' 'Thimbleberry' 'Appletini' 'Common bottlenose dolphin' 'Banana cream pie' 'Plastic wrap' 'Plastic bag' 'Newspaper' 'Waste collector' 'Red food coloring' 'Cherry liqueur' 'Food storage containers' 'African food' 'Street food' 'Black cherry' 'Plastic' 'Paper' 'Peruvian food' 'Tamil food' 'Strawberry tree' 'Dried cranberry' 'Surinam cherry' 'Tissue paper' 'Filipino food' 'Seafood' 'Processed food' 'Shanghai food' 'Red mulberry' 'Burmese food' 'Cranberry sauce' 'Vietnamese food' 'Southern united states food' 'Ceylon gooseberry' 'Strawberry' 'Virginia strawberry' 'Alpine strawberry' 'Strawberry juice' 'Thai food' 'Pineapple festival' 'Wallpaper paste' 'Tex-mex food' 'Vegetarian food' 'Turkish food' 'Mock strawberry' 'Pineapple bun' 'Paper cutter' 'Lingonberry jam' 'Cornelian cherry' 'Glass bottle' 'Cherry Tomatoes' 'Food group' 'Natural foods' 'Bushfood' 'Diet food' 'Toilet paper' 'Paper drilling' 'Banana' 'Construction paper' 'Italian food' 'Finger food' 'Food craving' 'Padang food' 'Waste container' 'Fried food' 'Pickled foods' 'Dog banana' 'Mango pudding' 'Food grain' 'Apple sauce' 'Blackberry pie' 'Whole food' 'Tibetan food' 'Oregon cherry' 'Hackberry' 'Apple dumpling' 'Banana cue' 'Mongolian food' 'Blueberry pie' 'Berry' 'Strawberry pie' 'Bird food' 'Banana ketchup' 'Banana leaf rice' 'Seafood boil' 'Two-liter bottle' 'Cherry' 'Mango' 'Pineapple' 'Banana powder' 'Juniper berry' 'Blueberry' 'Riberry' 'Saba banana' 'Armenian food' 'Food spoilage' 'Mango pickle' 'Australian food' 'Tayberry' 'Junk food' 'Paperweight' 'Art paper' 'Household paper product' 'Wrapping paper' 'Paper towel holder' 'Paper napkin' 'Waste containment' 'Small animal food' 'Paper product' 'Food warmer' 'Anchovy (food)' 'Blackberry' 'Shrimp and mango salad' 'Cranberry bean' --type_csv train --limit 8000