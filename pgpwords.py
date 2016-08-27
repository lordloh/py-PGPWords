#! /usr/bin/python
import sys
import re
import fileinput

def getPGPWords(givenString):
    pgpWords=[['aardvark','adroitness'],['absurd','adviser'],['accrue','aftermath'],['acme','aggregate'],['adrift','alkali'],['adult','almighty'],['afflict','amulet'],['ahead','amusement'],['aimless','antenna'],['Algol','applicant'],['allow','Apollo'],['alone','armistice'],['ammo','article'],['ancient','asteroid'],['apple','Atlantic'],['artist','atmosphere'],['assume','autopsy'],['Athens','Babylon'],['atlas','backwater'],['Aztec','barbecue'],['baboon','belowground'],['backfield','bifocals'],['backward','bodyguard'],['banjo','bookseller'],['beaming','borderline'],['bedlamp','bottomless'],['beehive','Bradbury'],['beeswax','bravado'],['befriend','Brazilian'],['Belfast','breakaway'],['berserk','Burlington'],['billiard','businessman'],['bison','butterfat'],['blackjack','Camelot'],['blockade','candidate'],['blowtorch','cannonball'],['bluebird','Capricorn'],['bombast','caravan'],['bookshelf','caretaker'],['brackish','celebrate'],['breadline','cellulose'],['breakup','certify'],['brickyard','chambermaid'],['briefcase','Cherokee'],['Burbank','Chicago'],['button','clergyman'],['buzzard','coherence'],['cement','combustion'],['chairlift','commando'],['chatter','company'],['checkup','component'],['chisel','concurrent'],['choking','confidence'],['chopper','conformist'],['Christmas','congregate'],['clamshell','consensus'],['classic','consulting'],['classroom','corporate'],['cleanup','corrosion'],['clockwork','councilman'],['cobra','crossover'],['commence','crucifix'],['concert','cumbersome'],['cowbell','customer'],['crackdown','Dakota'],['cranky','decadence'],['crowfoot','December'],['crucial','decimal'],['crumpled','designing'],['crusade','detector'],['cubic','detergent'],['dashboard','determine'],['deadbolt','dictator'],['deckhand','dinosaur'],['dogsled','direction'],['dragnet','disable'],['drainage','disbelief'],['dreadful','disruptive'],['drifter','distortion'],['dropper','document'],['drumbeat','embezzle'],['drunken','enchanting'],['Dupont','enrollment'],['dwelling','enterprise'],['eating','equation'],['edict','equipment'],['egghead','escapade'],['eightball','Eskimo'],['endorse','everyday'],['endow','examine'],['enlist','existence'],['erase','exodus'],['escape','fascinate'],['exceed','filament'],['eyeglass','finicky'],['eyetooth','forever'],['facial','fortitude'],['fallout','frequency'],['flagpole','gadgetry'],['flatfoot','Galveston'],['flytrap','getaway'],['fracture','glossary'],['framework','gossamer'],['freedom','graduate'],['frighten','gravity'],['gazelle','guitarist'],['Geiger','hamburger'],['glitter','Hamilton'],['glucose','handiwork'],['goggles','hazardous'],['goldfish','headwaters'],['gremlin','hemisphere'],['guidance','hesitate'],['hamlet','hideaway'],['highchair','holiness'],['hockey','hurricane'],['indoors','hydraulic'],['indulge','impartial'],['inverse','impetus'],['involve','inception'],['island','indigo'],['jawbone','inertia'],['keyboard','infancy'],['kickoff','inferno'],['kiwi','informant'],['klaxon','insincere'],['locale','insurgent'],['lockup','integrate'],['merit','intention'],['minnow','inventive'],['miser','Istanbul'],['Mohawk','Jamaica'],['mural','Jupiter'],['music','leprosy'],['necklace','letterhead'],['Neptune','liberty'],['newborn','maritime'],['nightbird','matchmaker'],['Oakland','maverick'],['obtuse','Medusa'],['offload','megaton'],['optic','microscope'],['orca','microwave'],['payday','midsummer'],['peachy','millionaire'],['pheasant','miracle'],['physique','misnomer'],['playhouse','molasses'],['Pluto','molecule'],['preclude','Montana'],['prefer','monument'],['preshrunk','mosquito'],['printer','narrative'],['prowler','nebula'],['pupil','newsletter'],['puppy','Norwegian'],['python','October'],['quadrant','Ohio'],['quiver','onlooker'],['quota','opulent'],['ragtime','Orlando'],['ratchet','outfielder'],['rebirth','Pacific'],['reform','pandemic'],['regain','Pandora'],['reindeer','paperweight'],['rematch','paragon'],['repay','paragraph'],['retouch','paramount'],['revenge','passenger'],['reward','pedigree'],['rhythm','Pegasus'],['ribcage','penetrate'],['ringbolt','perceptive'],['robust','performance'],['rocker','pharmacy'],['ruffled','phonetic'],['sailboat','photograph'],['sawdust','pioneer'],['scallion','pocketful'],['scenic','politeness'],['scorecard','positive'],['Scotland','potato'],['seabird','processor'],['select','provincial'],['sentence','proximate'],['shadow','puberty'],['shamrock','publisher'],['showgirl','pyramid'],['skullcap','quantity'],['skydive','racketeer'],['slingshot','rebellion'],['slowdown','recipe'],['snapline','recover'],['snapshot','repellent'],['snowcap','replica'],['snowslide','reproduce'],['solo','resistor'],['southward','responsive'],['soybean','retraction'],['spaniel','retrieval'],['spearhead','retrospect'],['spellbind','revenue'],['spheroid','revival'],['spigot','revolver'],['spindle','sandalwood'],['spyglass','sardonic'],['stagehand','Saturday'],['stagnate','savagery'],['stairway','scavenger'],['standard','sensation'],['stapler','sociable'],['steamship','souvenir'],['sterling','specialist'],['stockman','speculate'],['stopwatch','stethoscope'],['stormy','stupendous'],['sugar','supportive'],['surmount','surrender'],['suspense','suspicious'],['sweatband','sympathy'],['swelter','tambourine'],['tactics','telephone'],['talon','therapist'],['tapeworm','tobacco'],['tempest','tolerance'],['tiger','tomorrow'],['tissue','torpedo'],['tonic','tradition'],['topmost','travesty'],['tracker','trombonist'],['transit','truncated'],['trauma','typewriter'],['treadmill','ultimate'],['Trojan','undaunted'],['trouble','underfoot'],['tumor','unicorn'],['tunnel','unify'],['tycoon','universe'],['uncut','unravel'],['unearth','upcoming'],['unwind','vacancy'],['uproot','vagabond'],['upset','vertigo'],['upshot','Virginia'],['vapor','visitor'],['village','vocalist'],['virus','voyager'],['Vulcan','warranty'],['waffle','Waterloo'],['wallet','whimsical'],['watchword','Wichita'],['wayside','Wilmington'],['willow','Wyoming'],['woodlark','yesteryear'],['Zulu','Yucatan']];
    matchedHexString=re.findall('[0-9a-fA-F]+:.*:[0-9a-fA-F]+',givenString);
    if (len(matchedHexString)>0):
        numStr=matchedHexString[0].split(':');
        try:
            PGPWordsString='';
            i=1;
            for hexNum in numStr:
                PGPWordsString=PGPWordsString+' '+pgpWords[int(hexNum,16)][i%2];
                i=i+1;
            PGPWordsString=PGPWordsString.strip();
        except e:
            PGPWordsString=-2;
        return PGPWordsString;
    else:
        return -1;

def main():
    if (len(sys.argv)>1):
		if (sys.argv[1]=="--help"):
			print sys.argv[0]," [hex sting as 0A:0B:0C:DE:ED]"
			print "If you do not pass the hex string as a command line argument, you may pass it at sdtin use Ctrl+D to exit the script."
			pgpWords=0
		else:
			pgpWords=getPGPWords(sys.argv[1]);
    else:
        for line in fileinput.input():
            pgpWords=getPGPWords(line);
    if (isinstance(pgpWords, int)):
        return pgpWords;
    else:
        print pgpWords
        return 0;

if __name__ == "__main__":
    r=main()
    sys.exit(r)
