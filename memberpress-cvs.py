import re

# First set of input data
input_text_1 = """
Row 2: User (username=bob.clark@memorialhermann.org, ID=653) already existed and was updated successfully
Row 3: User (username=gina.mackey@memorialhermann.org, ID=647) already existed and was updated successfully
Row 4: User (username=annemarie.stakes@memorialhermann.org, ID=654) already existed and was updated successfully
Row 5: User (username=jacqueline.haggerty@memorialhermann.org, ID=655) already existed and was updated successfully
Row 6: User (username=joi.mcclure@memorialhermann.org, ID=656) already existed and was updated successfully
Row 7: User (username=buck.colomy@memorialhermann.org, ID=657) already existed and was updated successfully
Row 8: User (username=david.martin2@memorialhermann.org, ID=658) already existed and was updated successfully
Row 9: User (username=steve.soman@memorialhermann.org, ID=659) already existed and was updated successfully
Row 10: User (username=Robert.Clark@memorialhermann.org, ID=660) already existed and was updated successfully
Row 11: User (username=Stephanie.Osemwegie@memorialhermann.org, ID=661) already existed and was updated successfully
Row 12: User (username=Tawanda.Wilson@memorialhermann.org, ID=662) already existed and was updated successfully
Row 13: User (username=AnneMarie.Stakes@apex4health.com, ID=663) already existed and was updated successfully
Row 14: User (username=Melony.young@apex4health.com, ID=664) already existed and was updated successfully
Row 15: User (username=Wintana.Harness@memorialhermann.org, ID=665) already existed and was updated successfully
Row 16: User (username=jay.hurt2@memorialhermann.org, ID=666) already existed and was updated successfully
Row 17: User (username=Jay.Hurt@apex4health.com, ID=667) already existed and was updated successfully
Row 18: User (username=holly.turner@merck.com, ID=637) already existed and was updated successfully
Row 19: User (username=grace.pelkowski@merck.com, ID=641) already existed and was updated successfully
Row 20: User (username=jennifer.melchior@milliman.com, ID=627) already existed and was updated successfully
Row 21: User (username=fritz.busch@milliman.com, ID=651) already existed and was updated successfully
Row 22: User (username=raleigh.skaggs@milliman.com, ID=668) already existed and was updated successfully
Row 23: User (username=tim.lee@milliman.com, ID=669) already existed and was updated successfully
Row 24: User (username=jeff.milton-hall@milliman.com, ID=670) already existed and was updated successfully
Row 25: User (username=jason.nowakowski@milliman.com, ID=671) already existed and was updated successfully
Row 26: User (username=mary.creten@milliman.com, ID=672) already existed and was updated successfully
Row 27: User (username=paul.houchens@milliman.com, ID=673) already existed and was updated successfully
Row 28: User (username=bill.mckinley@milliman.com, ID=674) already existed and was updated successfully
Row 29: User (username=charlie.mills@milliman.com, ID=675) already existed and was updated successfully
Row 30: User (username=darin.muse@milliman.com, ID=676) already existed and was updated successfully
Row 31: User (username=ccliett@mwsgw.com, ID=640) already existed and was updated successfully
Row 32: User (username=bkitchin@mwlaw.com, ID=646) already existed and was updated successfully
Row 33: User (username=sstrickland@mwlaw.com, ID=639) already existed and was updated successfully
Row 34: User (username=rtredway@mwlaw.com, ID=677) already existed and was updated successfully
Row 35: User (username=rtredway@mwlaw.com, ID=677) already existed and was updated successfully
Row 36: User (username=mnored@mwlaw.com, ID=678) already existed and was updated successfully
Row 37: User (username=james_datz@mt-pharma-us.com, ID=621) already existed and was updated successfully
Row 38: User (username=william_gittinger@mt-pharma-us.com, ID=638) already existed and was updated successfully
Row 39: User (username=david_holman@mt-pharma-us.com, ID=679) already existed and was updated successfully
Row 40: User (username=scott.white@modahealth.com, ID=680) already existed and was updated successfully
Row 41: User (username=addy.binkley@modahealth.com, ID=681) already existed and was updated successfully
Row 42: User (username=Muriel.magee@modahealth.com, ID=682) already existed and was updated successfully
Row 43: User (username=James.light@modahealth.com, ID=683) already existed and was updated successfully
Row 44: User (username=Toni.ostrom@modahealth.com, ID=684) already existed and was updated successfully
Row 45: User (username=melisa.strong@modahealth.com, ID=685) already existed and was updated successfully
Row 46: User (username=Suzannah.dellacorte@modahealth.com, ID=686) already existed and was updated successfully
Row 47: User (username=Yale.popowich@modahealth.com, ID=687) already existed and was updated successfully
Row 48: User (username=Katie.scheelar@modahealth.com, ID=688) already existed and was updated successfully
Row 49: User (username=Carly.rodriguez@modahealth.com, ID=689) already existed and was updated successfully
Row 50: User (username=Cole.ahnberg@modahealth.com, ID=690) already existed and was updated successfully
Row 51: User (username=Katie.brokaw@modahealth.com, ID=691) already existed and was updated successfully
Row 52: User (username=Jason.gootee@modahealth.com, ID=692) already existed and was updated successfully
Row 53: User (username=theresa.barney@modahealth.com, ID=693) already existed and was updated successfully
Row 54: User (username=joe.greenman@modahealth.com, ID=694) already existed and was updated successfully
Row 55: User (username=sean.jessup@modahealth.com, ID=695) already existed and was updated successfully
Row 56: User (username=kayla.jones@modahealth.com, ID=696) already existed and was updated successfully
Row 57: User (username=stevenf@modivcare.com, ID=629) already existed and was updated successfully
Row 58: User (username=dennis.halmai@modivcare.com, ID=635) already existed and was updated successfully
Row 59: User (username=david.heckel@modivcare.com, ID=697) already existed and was updated successfully
Row 60: User (username=kathleen.payne@modivcare.com, ID=642) already existed and was updated successfully
Row 61: User (username=katherynn.fischer@logisticare.com, ID=698) already existed and was updated successfully
Row 62: User (username=phil.eades@modivcare.com, ID=699) already existed and was updated successfully
Row 63: User (username=brittany.haggstrom@modivcare.com, ID=700) already existed and was updated successfully
Row 64: User (username=michael.hankinson@modivcare.com, ID=701) already existed and was updated successfully
Row 65: User (username=carol.weil@molinahealthcare.com, ID=612) already existed and was updated successfully
Row 66: User (username=michelle.bentzien-purrington@molinahealthcare.com, ID=614) already existed and was updated successfully
Row 67: User (username=paul.sturm@molinahealthcare.com, ID=615) already existed and was updated successfully
Row 68: User (username=maharlika.delpilar@molinahealthcare.com, ID=617) already existed and was updated successfully
Row 69: User (username=cynthia.diaz1@molinahealthcare.com, ID=619) already existed and was updated successfully
Row 70: User (username=cameron.smyth@molinahealthcare.com, ID=624) already existed and was updated successfully
Row 71: User (username=kate.koons@molinahealthcare.com, ID=625) already existed and was updated successfully
Row 72: User (username=david.valdez1@molinahealthcare.com, ID=626) already existed and was updated successfully
Row 73: User (username=jim.locke@molinahealthcare.com, ID=630) already existed and was updated successfully
Row 74: User (username=gretchen.schuleman@molinahealthcare.com, ID=631) already existed and was updated successfully
Row 75: User (username=emran.rouf@molinahealthcare.com, ID=702) already existed and was updated successfully
Row 76: User (username=barbara.bagley@molinahealthcare.com, ID=703) already existed and was updated successfully
Row 77: User (username=hany.aziz@molinahealthcare.com, ID=704) already existed and was updated successfully
Row 78: User (username=naomi.alvarez@molinahealthcare.com, ID=705) already existed and was updated successfully
Row 79: User (username=joseph.vazhappilly@molinahealthcare.com, ID=648) already existed and was updated successfully
Row 80: User (username=carol.dobosh@molinahealthcare.com, ID=706) already existed and was updated successfully
Row 81: User (username=leticia.ramirez@molinahealthcare.com, ID=649) already existed and was updated successfully
Row 82: User (username=william.brendel@molinahealthcare.com, ID=707) already existed and was updated successfully
Row 83: User (username=cindy.fortress@molinahealthcare.com, ID=708) already existed and was updated successfully
Row 84: User (username=brandie.gasper@molinahealthcare.com, ID=709) already existed and was updated successfully
Row 85: User (username=robert.kalin@molinahealthcare.com, ID=710) already existed and was updated successfully
Row 86: User (username=caren.zysk@molinahealthcare.com, ID=711) already existed and was updated successfully
Row 87: User (username=brandi.mcmillan@molinahealthcare.com, ID=712) already existed and was updated successfully
Row 88: User (username=audrey.terry@molinahealthcare.com, ID=713) already existed and was updated successfully
Row 89: User (username=deliverytx@molinahealthcare.com, ID=714) already existed and was updated successfully
Row 90: User (username=gwendolyn.sowa@molinahealthcare.com, ID=715) already existed and was updated successfully
Row 91: User (username=rebecca.stokes@molinahealthcare.com, ID=716) already existed and was updated successfully
Row 92: User (username=caitlin.hogge2@molinahealthcare.com, ID=717) already existed and was updated successfully
Row 93: User (username=marie.dinh@molinahealthcare.com, ID=718) already existed and was updated successfully
Row 94: User (username=kathryn.chapman@molinahealthcare.com, ID=719) already existed and was updated successfully
Row 95: User (username=jeffrey.stone@molinahealthcare.com, ID=720) already existed and was updated successfully
Row 96: User (username=programmanagementhcs@molinahealthcare.com, ID=721) already existed and was updated successfully
Row 97: User (username=lauren.sorokolit@molinahealthcare.com, ID=722) already existed and was updated successfully
Row 98: User (username=shirley.bonney@molinahealthcare.com, ID=723) already existed and was updated successfully
Row 99: User (username=misha.lehman@molinahealthcare.com, ID=724) already existed and was updated successfully
Row 100: User (username=rachel.poe@molinahealthcare.com, ID=725) already existed and was updated successfully
Row 101: User (username=mark.shaffer@molinahealthcare.com, ID=726) already existed and was updated successfully
Row 102: User (username=Wendy.McGallion@molinahealthcare.com, ID=727) already existed and was updated successfully
Row 103: User (username=Denise.Arvia@molinahealthcare.com, ID=728) already existed and was updated successfully
Row 104: User (username=Mary.singer@molinahealthcare.com, ID=729) already existed and was updated successfully
Row 105: User (username=Marcy.Dickson@molinahealthcare.com, ID=730) already existed and was updated successfully
Row 106: User (username=Scott.albosta@molinahealthcare.com, ID=731) already existed and was updated successfully
Row 107: User (username=Kelsey.Letcher@molinahealthcare.com, ID=732) already existed and was updated successfully
Row 108: User (username=Rebecca.stokes@molinahealthcare.com, ID=716) already existed and was updated successfully
Row 109: User (username=Danita.Steward@molinahealthcare.com, ID=733) already existed and was updated successfully
Row 110: User (username=Loretta.Smith@molinahealthcare.com, ID=734) already existed and was updated successfully
Row 111: User (username=susan.weinfurther@molinahealthcare.com, ID=735) already existed and was updated successfully
Row 112: User (username=Nicole.Gonzales2@MolinaHealthCare.Com, ID=736) already existed and was updated successfully
Row 113: User (username=Susan.Weinfurther@molinahealthcare.com, ID=735) already existed and was updated successfully
Row 114: User (username=rosario.groomes@molinahealthcare.com, ID=737) already existed and was updated successfully
Row 115: User (username=susan.herndon@molinahealthcare.com, ID=738) already existed and was updated successfully
Row 116: User (username=julia.hamilton@molinahealthcare.com, ID=739) already existed and was updated successfully
Row 117: User (username=lindsey.vasquez@molinahealthcare.com, ID=740) already existed and was updated successfully
Row 118: User (username=jimmy.pan@molinahealthcare.com, ID=741) already existed and was updated successfully
Row 119: User (username=chris.coffey@molinahealthcare.com, ID=742) already existed and was updated successfully
Row 120: User (username=kelsey.letcher@molinahealthcare.com, ID=732) already existed and was updated successfully
Row 121: User (username=tania.colon@molinahealthcare.com, ID=743) already existed and was updated successfully
Row 122: User (username=bruce.lane@molinahealthcare.com, ID=744) already existed and was updated successfully
Row 123: User (username=mark.waggoner@momsmeals.com, ID=745) already existed and was updated successfully
Row 124: User (username=michaella.johnson@mossadams.com, ID=746) already existed and was updated successfully
Row 125: User (username=Brian.Conner@mossadams.com, ID=747) already existed and was updated successfully
Row 126: User (username=Rachel.Laureno@mossadams.com, ID=748) already existed and was updated successfully
Row 127: User (username=tony.andrade@mossadams.com, ID=749) already existed and was updated successfully
Row 128: User (username=William.norris@mossadams.com, ID=750) already existed and was updated successfully
Row 129: User (username=Josh.Lewis@mossadams.com, ID=751) already existed and was updated successfully
Row 130: User (username=ken@healthcrowd.com, ID=752) already existed and was updated successfully
Row 131: User (username=leslie@healthcrowd.com, ID=753) already existed and was updated successfully
Row 132: User (username=annemieke@healthcrowd.com, ID=754) already existed and was updated successfully
Row 133: User (username=bing@healthcrowd.com, ID=755) already existed and was updated successfully
Row 134: User (username=jackie@healthcrowd.com, ID=756) already existed and was updated successfully
Row 135: User (username=christian@healthcrowd.com, ID=757) already existed and was updated successfully
Row 136: User (username=josette@healthcrowd.com, ID=758) already existed and was updated successfully
Row 137: User (username=nora.cristobal@mpulsemobile.com, ID=759) already existed and was updated successfully
Row 138: User (username=alaina.tackett@mpulsemobile.com, ID=760) already existed and was updated successfully
Row 139: User (username=pstalboerger@mtm-inc.net, ID=761) already existed and was updated successfully
Row 140: User (username=jhericks@mtm-inc.net, ID=762) already existed and was updated successfully
Row 141: User (username=kprice@mtm-inc.net, ID=763) already existed and was updated successfully
Row 142: User (username=mlucas@mtm-inc.net, ID=764) already existed and was updated successfully
Row 143: User (username=joelsmith@mtm-inc.net, ID=765) already existed and was updated successfully
Row 144: User (username=ahazzard@e-nva.com, ID=766) already existed and was updated successfully
Row 145: User (username=rrenna@e-nva.com, ID=767) already existed and was updated successfully
Row 146: User (username=mgilmore@e-nva.com, ID=768) already existed and was updated successfully
Row 147: User (username=cmoroff@e-nva.com, ID=769) already existed and was updated successfully
Row 148: User (username=michelle.kroll@benecard.com, ID=770) already existed and was updated successfully
Row 149: User (username=ahazzard@e-nva.com, ID=766) already existed and was updated successfully
Row 150: User (username=mgilmore@e-nva.com, ID=768) already existed and was updated successfully
Row 151: User (username=david.fields@navitus.com, ID=771) already existed and was updated successfully
Row 152: User (username=sarah.schnell@navitus.com, ID=772) already existed and was updated successfully
Row 153: User (username=gayle.fisher@navitus.com, ID=773) already existed and was updated successfully
Row 154: User (username=collan.rosier@navitus.com, ID=774) already existed and was updated successfully
Row 155: User (username=byron.mickle@navitus.com, ID=775) already existed and was updated successfully
Row 156: User (username=rachel.breger@navitus.com, ID=776) already existed and was updated successfully
Row 157: User (username=michael.bevins@navitus.com, ID=777) already existed and was updated successfully
Row 158: User (username=donna.bentley@navitus.com, ID=778) already existed and was updated successfully
Row 159: User (username=tom.pabich@navitus.com, ID=779) already existed and was updated successfully
Row 160: User (username=tonnlarry@gmail.com, ID=780) already existed and was updated successfully
Row 161: User (username=robyn.crosson@navitus.com, ID=781) already existed and was updated successfully
Row 162: User (username=Kimberly.Rogers@navitus.com, ID=782) already existed and was updated successfully
Row 163: User (username=penny.avery@novartis.com, ID=783) already existed and was updated successfully
Row 164: User (username=jody.amodeo@novartis.com, ID=784) already existed and was updated successfully
Row 165: User (username=robert.zahid@novartis.com, ID=785) already existed and was updated successfully
Row 166: User (username=peter.trask@changehealthcare.com, ID=786) already existed and was updated successfully
Row 167: User (username=denise.louden@optum.com, ID=787) already existed and was updated successfully
Row 168: User (username=wally.danielson@optum.com, ID=788) already existed and was updated successfully
Row 169: User (username=fonsecah@advisory.com, ID=789) already existed and was updated successfully
Row 170: User (username=allison.pogue@optum.com, ID=790) already existed and was updated successfully
Row 171: User (username=yokleyb@advisory.com, ID=791) already existed and was updated successfully
Row 172: User (username=bglaeser@changehealthcare.com, ID=792) already existed and was updated successfully
Row 173: User (username=michael.creech@mckesson.com, ID=793) already existed and was updated successfully
Row 174: User (username=ahall@changehealthcare.com, ID=794) already existed and was updated successfully
Row 175: User (username=peter.firehammer@changehealthcare.com, ID=795) already existed and was updated successfully
Row 176: User (username=david.kaskoun@gmail.com, ID=796) already existed and was updated successfully
Row 177: User (username=chuck.wacker@optum.com, ID=797) already existed and was updated successfully
Row 178: User (username=bhoover@changehealthcare.com, ID=798) already existed and was updated successfully
Row 179: User (username=trebesn@advisory.com, ID=799) already existed and was updated successfully
Row 180: User (username=martha.herbig@optum.com, ID=800) already existed and was updated successfully
Row 181: User (username=phillip.king@changehealthcare.com, ID=801) already existed and was updated successfully
Row 182: User (username=dgallegos@changehealthcare.com, ID=802) already existed and was updated successfully
Row 183: User (username=kimsal@advisory.com, ID=803) already existed and was updated successfully
Row 184: User (username=susan.sivertsen@optum.com, ID=804) already existed and was updated successfully
Row 185: User (username=loren.koerber@optum.com, ID=805) already existed and was updated successfully
Row 186: User (username=Jessica.Marshall1@changehealthcare.com, ID=806) already existed and was updated successfully
Row 187: User (username=Candy.Chambers@changehealthcare.com, ID=807) already existed and was updated successfully
Row 188: User (username=WGeis@changehealthcare.com, ID=808) already existed and was updated successfully
Row 189: User (username=Danna.Ruppel@changehealthcare.com, ID=809) already existed and was updated successfully
Row 190: User (username=bewell@hioscar.com, ID=810) already existed and was updated successfully
Row 191: User (username=jslayton@hioscar.com, ID=811) already existed and was updated successfully
Row 192: User (username=meera@hioscar.com, ID=812) already existed and was updated successfully
Row 193: User (username=wjohnson@hioscar.com, ID=813) already existed and was updated successfully
Row 194: User (username=smartin@hioscar.com, ID=814) already existed and was updated successfully
Row 195: User (username=mpearce@hioscar.com, ID=815) already existed and was updated successfully
Row 196: User (username=kbaumann@hioscar.com, ID=816) already existed and was updated successfully
Row 197: User (username=csebastian@hioscar.com, ID=817) already existed and was updated successfully
Row 198: User (username=tward@hioscar.com, ID=818) already existed and was updated successfully
Row 199: User (username=missi@hioscar.com, ID=819) already existed and was updated successfully
Row 200: User (username=jvecchiet@hioscar.com, ID=820) already existed and was updated successfully
Row 201: User (username=rich@hioscar.com, ID=821) already existed and was updated successfully
Row 202: User (username=apapsun@hioscar.com, ID=822) already existed and was updated successfully
Row 203: User (username=jones@hioscar.com, ID=823) already existed and was updated successfully
Row 204: User (username=cgrason@hioscar.com, ID=824) already existed and was updated successfully
Row 205: User (username=alanna@hioscar.com, ID=825) already existed and was updated successfully
Row 206: User (username=mya@hioscar.com, ID=826) already existed and was updated successfully
Row 207: User (username=mario@hioscar.com, ID=827) already existed and was updated successfully
Row 208: User (username=krice@hioscar.com, ID=828) already existed and was updated successfully
Row 209: User (username=raxelrod@hioscar.com, ID=829) already existed and was updated successfully
Row 210: User (username=mpasnik@hioscar.com, ID=830) already existed and was updated successfully
Row 211: User (username=sorrange@hioscar.com, ID=831) already existed and was updated successfully
Row 212: User (username=jtredway@hioscar.com, ID=832) already existed and was updated successfully
Row 213: User (username=ava.norris@phhs.org, ID=833) already existed and was updated successfully
Row 214: User (username=khurram.taufiq@phhs.org, ID=834) already existed and was updated successfully
Row 215: User (username=david.bartoszek@phhs.org, ID=835) already existed and was updated successfully
Row 216: User (username=amrita.waingankar@phhs.org, ID=836) already existed and was updated successfully
Row 217: User (username=tamara.willie@phhs.org, ID=837) already existed and was updated successfully
Row 218: User (username=margaret.roche@phhs.org, ID=838) already existed and was updated successfully
Row 219: User (username=peter.waziri@phhs.org, ID=839) already existed and was updated successfully
Row 220: User (username=nicholas.smith@phhs.org, ID=840) already existed and was updated successfully
Row 221: User (username=nakia.smith@phhs.org, ID=841) already existed and was updated successfully
Row 222: User (username=andrew.shapiro@phhs.org, ID=842) already existed and was updated successfully
Row 223: User (username=tamara.gavin@phhs.org, ID=843) already existed and was updated successfully
Row 224: User (username=kellie.philpot@phhs.org, ID=844) already existed and was updated successfully
Row 225: User (username=justin.skerbetz@phhs.org, ID=845) already existed and was updated successfully
Row 226: User (username=paula.turicchi@phhs.org, ID=846) already existed and was updated successfully
Row 227: User (username=jeniffer.gonzalez@phhs.org, ID=847) already existed and was updated successfully
Row 228: User (username=melissa.zook@phhs.org, ID=848) already existed and was updated successfully
Row 229: User (username=michael.deluna@phhs.org, ID=849) already existed and was updated successfully
Row 230: User (username=jane.stegall@phhs.org, ID=850) already existed and was updated successfully
Row 231: User (username=susan.libson@phhs.org, ID=851) already existed and was updated successfully
Row 232: User (username=lee.deluna@phhs.org, ID=852) already existed and was updated successfully
Row 233: User (username=felicia.ramirez@phhs.org, ID=853) already existed and was updated successfully
Row 234: User (username=cheryl.edwards@phhs.org, ID=854) already existed and was updated successfully
Row 235: User (username=karshena.valsin@phhs.org, ID=855) already existed and was updated successfully
Row 236: User (username=Reigen.lox@phhs.org, ID=856) already existed and was updated successfully
Row 237: User (username=paula.turicchi@gmail.com, ID=857) already existed and was updated successfully
Row 238: User (username=Jill.terrymichener@phhs.org, ID=858) already existed and was updated successfully
Row 239: User (username=suzanne.faulkenberry@phhs.org, ID=859) already existed and was updated successfully
Row 240: User (username=amanda.hudgens@phhs.org, ID=860) already existed and was updated successfully
Row 241: User (username=NEEL.PATEL@phhs.org, ID=861) already existed and was updated successfully
Row 242: User (username=reigen.lox@phhs.org, ID=856) already existed and was updated successfully
Row 243: User (username=Victoria.Mora@phhs.org, ID=81) already existed and was updated successfully
Row 244: User (username=Amanda.hudgens@phhs.org, ID=860) already existed and was updated successfully
Row 245: User (username=graham.keever@phhs.org, ID=862) already existed and was updated successfully
Row 246: User (username=katherine.yoder@phhs.org, ID=863) already existed and was updated successfully
Row 247: User (username=tom.murar@phhs.org, ID=864) already existed and was updated successfully
Row 248: User (username=gordon.davis@phhs.org, ID=865) already existed and was updated successfully
Row 249: User (username=mshrader@pcmanet.org, ID=866) already existed and was updated successfully
Row 250: User (username=pfjelstad@pcmanet.org, ID=867) already existed and was updated successfully
Row 251: User (username=me@mindyellmer.com, ID=868) already existed and was updated successfully
Row 252: User (username=kim@podimetrics.com, ID=869) already existed and was updated successfully
Row 253: User (username=simon@podimetrics.com, ID=870) already existed and was updated successfully
Row 254: User (username=nicole@podimetrics.com, ID=871) already existed and was updated successfully
Row 255: User (username=jon@podimetrics.com, ID=872) already existed and was updated successfully
Row 256: User (username=davidica@podimetrics.com, ID=873) already existed and was updated successfully
Row 257: User (username=droot@primetherapeutics.com, ID=874) already existed and was updated successfully
Row 258: User (username=ptwohy@primetherapeutics.com, ID=875) already existed and was updated successfully
Row 259: User (username=lmendezharper@primetherapeutics.com, ID=876) already existed and was updated successfully
Row 260: User (username=caitlin.berry@primetherapeutics.com, ID=877) already existed and was updated successfully
Row 261: User (username=jamo.rubin@rightsitehealth.com, ID=878) already existed and was updated successfully
Row 262: User (username=jamo.rubin@rightsitehealth.com, ID=878) already existed and was updated successfully
Row 263: User (username=robbins@saferidehealth.com, ID=879) already existed and was updated successfully
Row 264: User (username=josh@saferidehealth.com, ID=880) already existed and was updated successfully
Row 265: User (username=patrick@saferidehealth.com, ID=881) already existed and was updated successfully
Row 266: User (username=andy@saferidehealth.com, ID=882) already existed and was updated successfully
Row 267: User (username=carolyn@saferidehealth.com, ID=883) already existed and was updated successfully
Row 268: User (username=david@saferidehealth.com, ID=884) already existed and was updated successfully
Row 269: User (username=ben@saferidehealth.com, ID=885) already existed and was updated successfully
Row 270: User (username=ashley@saferidehealth.com, ID=886) already existed and was updated successfully
Row 271: User (username=dpipkin@sarepta.com, ID=887) already existed and was updated successfully
Row 272: User (username=ccaldwell@sarepta.com, ID=888) already existed and was updated successfully
Row 273: User (username=swhite@scanhealthplan.com, ID=889) already existed and was updated successfully
Row 274: User (username=GHawkins@scanhealthplan.com, ID=890) already existed and was updated successfully
Row 275: User (username=DHoward@scanhealthplan.com, ID=891) already existed and was updated successfully
Row 276: User (username=WZhao@scanhealthplan.com, ID=892) already existed and was updated successfully
Row 277: User (username=s.ramalingam@bswhealth.org, ID=893) already existed and was updated successfully
Row 278: User (username=cathy.caswell@bswhealth.org, ID=894) already existed and was updated successfully
Row 279: User (username=amber.burgos@bswhealth.org, ID=895) already existed and was updated successfully
Row 280: User (username=maureen.martin@bswhealth.org, ID=896) already existed and was updated successfully
Row 281: User (username=sharon.saravia@bswhealth.org, ID=897) already existed and was updated successfully
Row 282: User (username=felicia.smith@bswhealth.org, ID=898) already existed and was updated successfully
Row 283: User (username=karen.baratta@bswhealth.org, ID=899) already existed and was updated successfully
Row 284: User (username=david.ellis@bswhealth.org, ID=900) already existed and was updated successfully
Row 285: User (username=basma.khurshid@bswhealth.org, ID=901) already existed and was updated successfully
Row 286: User (username=susan.balezentis@bswhealth.org, ID=902) already existed and was updated successfully
Row 287: User (username=amy.cornett@bswhealth.org, ID=903) already existed and was updated successfully
Row 288: User (username=vilaida.rivera@bswhealth.org, ID=904) already existed and was updated successfully
Row 289: User (username=dipali.portwood@bswhealth.org, ID=905) already existed and was updated successfully
Row 290: User (username=lisa.fillip@bswhealth.org, ID=906) already existed and was updated successfully
Row 291: User (username=mary.field@bswhealth.org, ID=907) already existed and was updated successfully
Row 292: User (username=natalie.rivera@bswhealth.org, ID=908) already existed and was updated successfully
Row 293: User (username=danielle.jaber@bswhealth.org, ID=909) already existed and was updated successfully
Row 294: User (username=erica.martin@bswhealth.org, ID=910) already existed and was updated successfully
Row 295: User (username=lauren.russell1@bswhealth.org, ID=911) already existed and was updated successfully
Row 296: User (username=chastidy.artis@bswhealth.org, ID=912) already existed and was updated successfully
Row 297: User (username=marisa.finley@bswhealth.org, ID=913) already existed and was updated successfully
Row 298: User (username=evelyn.gabrillo@bswhealth.org, ID=914) already existed and was updated successfully
Row 299: User (username=lindsay.manning@bswhealth.org, ID=915) already existed and was updated successfully
Row 300: User (username=theresa.magellan@bswhealth.org, ID=916) already existed and was updated successfully
Row 301: User (username=megan.cunningham@bswhealth.org, ID=917) already existed and was updated successfully
Row 302: User (username=jessica.sullivan1@bswhealth.org, ID=918) already existed and was updated successfully
Row 303: User (username=timothy.tasset@bswhealth.org, ID=919) already existed and was updated successfully
Row 304: User (username=elizabeth.lopezcepero@bswhealth.org, ID=920) already existed and was updated successfully
Row 305: User (username=kristi.sherrill@bswhealth.org, ID=921) already existed and was updated successfully
Row 306: User (username=stacey.byrd@bswhealth.org, ID=922) already existed and was updated successfully
Row 307: User (username=ellen.verzino@bswhealth.org, ID=923) already existed and was updated successfully
Row 308: User (username=leonardo.gutierrez@bswhealth.org, ID=924) already existed and was updated successfully
Row 309: User (username=jason.tipton@bswhealth.org, ID=925) already existed and was updated successfully
Row 310: User (username=mico.adams@bswhealth.org, ID=926) already existed and was updated successfully
Row 311: User (username=kathleen.martin@bswhealth.org, ID=927) already existed and was updated successfully
Row 312: User (username=ira.bell@bswhealth.org, ID=928) already existed and was updated successfully
Row 313: User (username=david.krauss@bswhealth.org, ID=929) already existed and was updated successfully
Row 314: User (username=Chmyra.Starks@BSWHealth.org, ID=930) already existed and was updated successfully
Row 315: User (username=Jenny.Garcia1@bswhealth.org, ID=931) already existed and was updated successfully
Row 316: User (username=charlotte.luebbert@BSWhealth.org, ID=932) already existed and was updated successfully
Row 317: User (username=daniel.posey@bswhealth.org, ID=933) already existed and was updated successfully
Row 318: User (username=lydia.best@bswhealth.org, ID=934) already existed and was updated successfully
Row 319: User (username=SUBROWN@sw.org, ID=935) already existed and was updated successfully
Row 320: User (username=wendy.brownlee@bswhealth.org, ID=936) already existed and was updated successfully
Row 321: User (username=Amanda.Pittman@bswhealth.org, ID=937) already existed and was updated successfully
Row 322: User (username=Jennifer.Boreing@bswhealth.org, ID=938) already existed and was updated successfully
Row 323: User (username=Kristy.Bulhoes@bswhealth.org, ID=939) already existed and was updated successfully
Row 324: User (username=Tara.Stafford@bswhealth.org, ID=940) already existed and was updated successfully
Row 325: User (username=Richard.Reuter@bswhealth.org, ID=941) already existed and was updated successfully
Row 326: User (username=John.Majors@bswhealth.org, ID=942) already existed and was updated successfully
Row 327: User (username=sirika.clayton@bswhealth.org, ID=943) already existed and was updated successfully
Row 328: User (username=Neil.Bhakta@bswhealth.org, ID=944) already existed and was updated successfully
Row 329: User (username=heather.ueckert@bswhealth.org, ID=945) already existed and was updated successfully
Row 330: User (username=opal.galliano@bswhealth.org, ID=946) already existed and was updated successfully
Row 331: User (username=elizabeth.lopezcepero@bswhealth.org, ID=920) already existed and was updated successfully
Row 332: User (username=Kimberley.Adda@bswhealth.org, ID=947) already existed and was updated successfully
Row 333: User (username=Anita.Hart@bswhealth.org, ID=948) already existed and was updated successfully
Row 334: User (username=anita.hart@bswhealth.org, ID=948) already existed and was updated successfully
Row 335: User (username=Stacie.walkerposvar@bswhealth.org, ID=949) already existed and was updated successfully
Row 336: User (username=Amanda.Trapasso@BSWHealth.org, ID=950) already existed and was updated successfully
Row 337: User (username=laci.noble@bswhealth.org, ID=951) already existed and was updated successfully
Row 338: User (username=Nichole.Whited@bswhealth.org, ID=952) already existed and was updated successfully
Row 339: User (username=Cristal.Detert@bswhealth.org, ID=953) already existed and was updated successfully
Row 340: User (username=Roger.HarrisPates@bswhealth.org, ID=954) already existed and was updated successfully
Row 341: User (username=Andrew.Berg@bswhealth.org, ID=955) already existed and was updated successfully
Row 342: User (username=Patsy.Vrazel@bswhealth.org, ID=956) already existed and was updated successfully
Row 343: User (username=Tracie.Acosta@bswhealth.org, ID=957) already existed and was updated successfully
Row 344: User (username=Esther.Webb@bswhealth.org, ID=958) already existed and was updated successfully
Row 345: User (username=melissa.rosson@bswhealth.org, ID=959) already existed and was updated successfully
Row 346: User (username=jeffrey.ingrum@bswhealth.org, ID=960) already existed and was updated successfully
Row 347: User (username=deborah.cotton@bswhealth.org, ID=961) already existed and was updated successfully
Row 348: User (username=tamara.caldwell@bswhealth.org, ID=962) already existed and was updated successfully
Row 349: User (username=jessica.olson2@bswhealth.org, ID=963) already existed and was updated successfully
Row 350: User (username=suzanne.brown@bswhealth.org, ID=964) already existed and was updated successfully
Row 351: User (username=jesse.sifuentez@bswhealth.org, ID=965) already existed and was updated successfully
Row 352: User (username=gjessee@sellersdorsey.com, ID=966) already existed and was updated successfully
Row 353: User (username=tko@sellersdorsey.com, ID=967) already existed and was updated successfully
Row 354: User (username=jfagen@sellersdorsey.com, ID=968) already existed and was updated successfully
Row 355: User (username=sludher@sellersdorsey.com, ID=969) already existed and was updated successfully
Row 356: User (username=pamela.piatt@senderohealth.com, ID=970) already existed and was updated successfully
Row 357: User (username=rosemary.ang@senderohealth.com, ID=971) already existed and was updated successfully
Row 358: User (username=ashlea.tolbert@senderohealth.com, ID=972) already existed and was updated successfully
Row 359: User (username=misty.smith@senderohealth.com, ID=973) already existed and was updated successfully
Row 360: User (username=perla.cavazos@centralhealth.net, ID=974) already existed and was updated successfully
Row 361: User (username=theresa.bedinghaus@senderohealth.com, ID=975) already existed and was updated successfully
Row 362: User (username=alfonso.rubio@senderohealth.com, ID=976) already existed and was updated successfully
Row 363: User (username=stephanie.mendez@senderohealth.com, ID=977) already existed and was updated successfully
Row 364: User (username=stacy.leon@senderohealth.com, ID=978) already existed and was updated successfully
Row 365: User (username=yaremi.cortez@senderohealth.com, ID=979) already existed and was updated successfully
Row 366: User (username=compliance@senderohealth.com, ID=980) already existed and was updated successfully
Row 367: User (username=marycarol.jennings@senderohealth.com, ID=981) already existed and was updated successfully
Row 368: User (username=amber.allbritten@senderohealth.com, ID=982) already existed and was updated successfully
Row 369: User (username=ted.held@senderohealth.com, ID=983) already existed and was updated successfully
Row 370: User (username=rodolfor.ybarra@senderohealth.com, ID=984) already existed and was updated successfully
Row 371: User (username=elizabeth.barreneche@senderohealth.com, ID=985) already existed and was updated successfully
Row 372: User (username=tierra.thomas@senderohealth.com, ID=986) already existed and was updated successfully
Row 373: User (username=celso.baez@centralhealth.net, ID=987) already existed and was updated successfully
Row 374: User (username=pastora.galvez@senderohealth.com, ID=988) already existed and was updated successfully
Row 375: User (username=matthew.keats@senderohealth.com, ID=989) already existed and was updated successfully
Row 376: User (username=Yvette.Bates-Coleman@senderohealth.com, ID=990) already existed and was updated successfully
Row 377: User (username=Paul.Emerson@centralhealth.net, ID=991) already existed and was updated successfully
Row 378: User (username=Perla.Cavazos@senderohealth.com, ID=992) already existed and was updated successfully
Row 379: User (username=charles.gilham@ascension.org, ID=993) already existed and was updated successfully
Row 380: User (username=adean2@ascension.org, ID=994) already existed and was updated successfully
Row 381: User (username=saszucs@ascension.org, ID=995) already existed and was updated successfully
Row 382: User (username=tkillebrew@ascension.org, ID=996) already existed and was updated successfully
Row 383: User (username=akennedy@ascension.org, ID=997) already existed and was updated successfully
Row 384: User (username=janet.walker@ascension.org, ID=998) already existed and was updated successfully
Row 385: User (username=emiliano.romero@ascension.org, ID=999) already existed and was updated successfully
Row 386: User (username=kaedwards@ascension.org, ID=1000) already existed and was updated successfully
Row 387: User (username=aromero@ascension.org, ID=1001) already existed and was updated successfully
Row 388: User (username=grodriguez1@ascension.org, ID=1002) already existed and was updated successfully
Row 389: User (username=suffelman@ascension.org, ID=1003) already existed and was updated successfully
Row 390: User (username=sharon.jandrain@ascension.org, ID=1004) already existed and was updated successfully
Row 391: User (username=Sara.Daugherty@ascension.org, ID=1005) already existed and was updated successfully
Row 392: User (username=kristine.norris@ascension.org, ID=1006) already existed and was updated successfully
Row 393: User (username=susan.balezentis@ascension.org, ID=1007) already existed and was updated successfully
Row 394: User (username=adolfo.valadez@ascension.org, ID=1008) already existed and was updated successfully
Row 395: User (username=mvnguyen2@ascension.org, ID=1009) already existed and was updated successfully
Row 396: User (username=sara.daugherty@ascension.org, ID=1005) already existed and was updated successfully
Row 397: User (username=cynthia.davis1@ascension.org, ID=1010) already existed and was updated successfully
Row 398: User (username=nicole.nealey@ascension.org, ID=1011) already existed and was updated successfully
Row 399: User (username=marinan.williams@ascension.org, ID=1012) already existed and was updated successfully
Row 400: User (username=rosievmcstay@rvmstrategies.net, ID=1013) already existed and was updated successfully
Row 401: User (username=paul.tannos@ascension.org, ID=1014) already existed and was updated successfully
Row 402: User (username=marc.parker@sunovion.com, ID=1015) already existed and was updated successfully
Row 403: User (username=scott.hylla@sunovion.com, ID=1016) already existed and was updated successfully
Row 404: User (username=mario.freeman@sunovion.com, ID=1017) already existed and was updated successfully
Row 405: User (username=jeffrey.simon@superiorhealthplan.com, ID=1018) already existed and was updated successfully
Row 406: User (username=cleo.diom@superiorhealthplan.com, ID=1019) already existed and was updated successfully
Row 407: User (username=albert@hawkinsppc.com, ID=1020) already existed and was updated successfully
Row 408: User (username=rachelle.palima@superiorhealthplan.com, ID=1021) already existed and was updated successfully
Row 409: User (username=shan.song@centene.com, ID=1022) already existed and was updated successfully
Row 410: User (username=esmeralda.cazares-baig@superiorhealthplan.com, ID=1023) already existed and was updated successfully
Row 411: User (username=allison.swartz@superiorhealthplan.com, ID=1024) already existed and was updated successfully
Row 412: User (username=patricia.correa@superiorhealthplan.com, ID=74) already existed and was updated successfully
Row 413: User (username=tracy.rico@superiorhealthplan.com, ID=1025) already existed and was updated successfully
Row 414: User (username=calvin.williams@superiorhealthplan.com, ID=1026) already existed and was updated successfully
Row 415: User (username=jocelyn.zimmerle@superiorhealthplan.com, ID=1027) already existed and was updated successfully
Row 416: User (username=narcedalia.aguayo@superiorhealthplan.com, ID=1028) already existed and was updated successfully
Row 417: User (username=angel.duran@superiorhealthplan.com, ID=1029) already existed and was updated successfully
Row 418: User (username=john.waidner@superiorhealthplan.com, ID=1030) already existed and was updated successfully
Row 419: User (username=alex.goldson@superiorhealthplan.com, ID=1031) already existed and was updated successfully
Row 420: User (username=amanda.r.shaw@centene.com, ID=1032) already existed and was updated successfully
Row 421: User (username=mraleigh@centene.com, ID=1033) already existed and was updated successfully
Row 422: User (username=brendle.glomb@superiorhealthplan.com, ID=1034) already existed and was updated successfully
Row 423: User (username=lacy.slaughter@superiorhealthplan.com, ID=1035) already existed and was updated successfully
Row 424: User (username=malinda.buratti@superiorhealthplan.com, ID=1036) already existed and was updated successfully
Row 425: User (username=ben.hamm@superiorhealthplan.com, ID=1037) already existed and was updated successfully
Row 426: User (username=robert.barone@superiorhealthplan.com, ID=1038) already existed and was updated successfully
Row 427: User (username=jenmiller@centene.com, ID=1039) already existed and was updated successfully
Row 428: User (username=michelle.murdock@superiorhealthplan.com, ID=1040) already existed and was updated successfully
Row 429: User (username=rene.pena2@superiorhealthplan.com, ID=1041) already existed and was updated successfully
Row 430: User (username=teresa.kahan@superiorhealthplan.com, ID=1042) already existed and was updated successfully
Row 431: User (username=julie.smith@superiorhealthplan.com, ID=1043) already existed and was updated successfully
Row 432: User (username=karen.westbay@superiorhealthplan.com, ID=1044) already existed and was updated successfully
Row 433: User (username=reed@crestline-solutions.com, ID=1045) already existed and was updated successfully
Row 434: User (username=dkillian@centene.com, ID=1046) already existed and was updated successfully
Row 435: User (username=cari.cates@superiorhealthplan.com, ID=1047) already existed and was updated successfully
Row 436: User (username=james.m.robson@centene.com, ID=1048) already existed and was updated successfully
Row 437: User (username=regulatory.compliance@superiorhealthplan.com, ID=1049) already existed and was updated successfully
Row 438: User (username=tanya.wells@superiorhealthplan.com, ID=72) already existed and was updated successfully
Row 439: User (username=perla.arce-franke@superiorhealthplan.com, ID=1050) already existed and was updated successfully
Row 440: User (username=jennifer.gasior@superiorhealthplan.com, ID=1051) already existed and was updated successfully
Row 441: User (username=marissa.livingston@superiorhealthplan.com, ID=1052) already existed and was updated successfully
Row 442: User (username=vanessa.sportsman@superiorhealthplan.com, ID=1053) already existed and was updated successfully
Row 443: User (username=albert.lopez@superiorhealthplan.com, ID=79) already existed and was updated successfully
Row 444: User (username=jennifer.shipman@superiorhealthplan.com, ID=1054) already existed and was updated successfully
Row 445: User (username=sara.robins@superiorhealthplan.com, ID=1055) already existed and was updated successfully
Row 446: User (username=michelle.mitchell@superiorhealthplan.com, ID=1056) already existed and was updated successfully
Row 447: User (username=susan.deville@superiorhealthplan.com, ID=1057) already existed and was updated successfully
Row 448: User (username=debra.danziger@superiorhealthplan.com, ID=1058) already existed and was updated successfully
Row 449: User (username=rowells@centene.com, ID=1059) already existed and was updated successfully
Row 450: User (username=ambar.qureshi@superiorhealthplan.com, ID=1060) already existed and was updated successfully
Row 451: User (username=cecilia.barraza@superiorhealthplan.com, ID=1061) already existed and was updated successfully
Row 452: User (username=patrick.kovalik@superiorhealthplan.com, ID=1062) already existed and was updated successfully
Row 453: User (username=destine.rawls@superiorhealthplan.com, ID=1063) already existed and was updated successfully
Row 454: User (username=kfreeman@centene.com, ID=1064) already existed and was updated successfully
Row 455: User (username=anna.velasquez@superiorhealthplan.com, ID=1065) already existed and was updated successfully
Row 456: User (username=lenore.depagter@superiorhealthplan.com, ID=1066) already existed and was updated successfully
Row 457: User (username=cheryl.cizler@superiorhealthplan.com, ID=1067) already existed and was updated successfully
Row 458: User (username=denise.herrera@superiorhealthplan.com, ID=1068) already existed and was updated successfully
Row 459: User (username=shereen.jensen@wellcare.com, ID=1069) already existed and was updated successfully
Row 460: User (username=jenn@phenixsaenz.com, ID=83) already existed and was updated successfully
Row 461: User (username=sandra.vale@superiorhealthplan.com, ID=84) already existed and was updated successfully
Row 462: User (username=cathy@schluetergroup.com, ID=1070) already existed and was updated successfully
Row 463: User (username=tom.shock@superiorhealthplan.com, ID=1071) already existed and was updated successfully
Row 464: User (username=sara.pena@superiorhealthplan.com, ID=1072) already existed and was updated successfully
Row 465: User (username=evett.bayles@superiorhealthplan.com, ID=1073) already existed and was updated successfully
Row 466: User (username=maryann.haddad@superiorhealthplan.com, ID=1074) already existed and was updated successfully
Row 467: User (username=chartaimer.mcqueen@superiorhealthplan.com, ID=1075) already existed and was updated successfully
Row 468: User (username=micah.smith@superiorhealthplan.com, ID=1076) already existed and was updated successfully
Row 469: User (username=colleen.gossling@superiorhealthplan.com, ID=1077) already existed and was updated successfully
Row 470: User (username=lspence@hslawmail.com, ID=80) already existed and was updated successfully
Row 471: User (username=emily.elizarde@superiorhealthplan.com, ID=1078) already existed and was updated successfully
Row 472: User (username=karen.f.blizzardmarsh@superiorhealthplan.com, ID=1079) already existed and was updated successfully
Row 473: User (username=arnulfo.rios@superiorhealthplan.com, ID=1080) already existed and was updated successfully
Row 474: User (username=valerie.chapa@superiorhealthplan.com, ID=1081) already existed and was updated successfully
Row 475: User (username=kathleen.ballee@superiorhealthplan.com, ID=1082) already existed and was updated successfully
Row 476: User (username=jessica.najera@superiorhealthplan.com, ID=1083) already existed and was updated successfully
Row 477: User (username=andrea.gillentine@superiorhealthplan.com, ID=1084) already existed and was updated successfully
Row 478: User (username=andrea.brambila@superiorhealthplan.com, ID=1085) already existed and was updated successfully
Row 479: User (username=orlando.julian@superiorhealthplan.com, ID=1086) already existed and was updated successfully
Row 480: User (username=valerie.gates@superiorhealthplan.com, ID=86) already existed and was updated successfully
Row 481: User (username=porcha.pulley@superiorhealthplan.com, ID=1087) already existed and was updated successfully
Row 482: User (username=jennifer.alanis@superiorhealthplan.com, ID=1088) already existed and was updated successfully
Row 483: User (username=stan@schluetergroup.com, ID=1089) already existed and was updated successfully
Row 484: User (username=veronica.laduc@superiorhealthplan.com, ID=1090) already existed and was updated successfully
Row 485: User (username=kenneth.james@superiorhealthplan.com, ID=1091) already existed and was updated successfully
Row 486: User (username=ryan.mckenna@superiorhealthplan.com, ID=1092) already existed and was updated successfully
Row 487: User (username=thomas.nguyen@superiorhealthplan.com, ID=1093) already existed and was updated successfully
Row 488: User (username=brad@schluetergroup.com, ID=1094) already existed and was updated successfully
Row 489: User (username=holly.munin@superiorhealthplan.com, ID=1095) already existed and was updated successfully
Row 490: User (username=verna.pratt@superiorhealthplan.com, ID=1096) already existed and was updated successfully
Row 491: User (username=robert.wilson@superiorhealthplan.com, ID=1097) already existed and was updated successfully
Row 492: User (username=ceseley.rollins@superiorhealthplan.com, ID=1098) already existed and was updated successfully
Row 493: User (username=troy.riley@superiorhealthplan.com, ID=1099) already existed and was updated successfully
Row 494: User (username=david.harmon@superiorhealthplan.com, ID=1100) already existed and was updated successfully
Row 495: User (username=charles.dubose@superiorhealthplan.com, ID=1101) already existed and was updated successfully
Row 496: User (username=michael.cation@superiorhealthplan.com, ID=1102) already existed and was updated successfully
Row 497: User (username=ryan.link@centene.com, ID=1103) already existed and was updated successfully
Row 498: User (username=jason.mcbride@superiorhealthplan.com, ID=1104) already existed and was updated successfully
Row 499: User (username=jeremy.lloyd@superiorhealthplan.com, ID=1105) already existed and was updated successfully
Row 500: User (username=twise@centene.com, ID=1106) already existed and was updated successfully
Row 501: User (username=francie.wambua@superiorhealthplan.com, ID=1107) already existed and was updated successfully
Row 502: User (username=amy.meyers@superiorhealthplan.com, ID=1108) already existed and was updated successfully
Row 503: User (username=tammy.c.edwards@centene.com, ID=1109) already existed and was updated successfully
Row 504: User (username=kia.biller@superiorhealthplan.com, ID=1110) already existed and was updated successfully
Row 505: User (username=cynthia.rojas@superiorhealthplan.com, ID=1111) already existed and was updated successfully
Row 506: User (username=michelle.fouche@superiorhealthplan.com, ID=1112) already existed and was updated successfully
Row 507: User (username=sarah.esquivel@superiorhealthplan.com, ID=1113) already existed and was updated successfully
Row 508: User (username=lesa.warren@superiorhealthplan.com, ID=1114) already existed and was updated successfully
Row 509: User (username=sarah.sorensen@superiorhealthplan.com, ID=1115) already existed and was updated successfully
Row 510: User (username=robert.wilson@superiorhealthplan.com, ID=1097) already existed and was updated successfully
Row 511: User (username=vicki.estrada@superiorhealthplan.com, ID=1116) already existed and was updated successfully
Row 512: User (username=rachael.przybyla@superiorhealthplan.com, ID=78) already existed and was updated successfully
Row 513: User (username=michael.diel@superiorhealthplan.com, ID=1117) already existed and was updated successfully
Row 514: User (username=natalie.hernandez@superiorhealthplan.com, ID=1118) already existed and was updated successfully
Row 515: User (username=jessica.estrada@superiorhealthplan.com, ID=87) already existed and was updated successfully
Row 516: User (username=jonathan.gallop@superiorhealthplan.com, ID=1119) already existed and was updated successfully
Row 517: User (username=jennifer.e.nehrkorn@superiorhealthplan.com, ID=1120) already existed and was updated successfully
Row 518: User (username=kcalvert@centene.com, ID=1121) already existed and was updated successfully
Row 519: User (username=noemi.smithroat@superiorhealthplan.com, ID=1122) already existed and was updated successfully
Row 520: User (username=Taylor.Cooper@CENTENE.COM, ID=1123) already existed and was updated successfully
Row 521: User (username=Saul.Ortega@superiorhealthplan.com, ID=1124) already existed and was updated successfully
Row 522: User (username=marina.fahim@superiorhealth.com, ID=1125) already existed and was updated successfully
Row 523: User (username=Katheryn.Johnson@superiorhealthplan.com, ID=1126) already existed and was updated successfully
Row 524: User (username=gavin@gavinmassingill.com, ID=1127) already existed and was updated successfully
Row 525: User (username=Teresa.Gonzales@superiorhealthplan.com, ID=1128) already existed and was updated successfully
Row 526: User (username=Nicole.M.Hoffman@superiorhealthplan.com, ID=1129) already existed and was updated successfully
Row 527: User (username=Nathan.Hoover@superiorhealthplan.com, ID=1130) already existed and was updated successfully
Row 528: User (username=Dan.Horn@superiorhealthplan.com, ID=1131) already existed and was updated successfully
Row 529: User (username=dana.chothmounethinh@superiorhealthplan.com, ID=1132) already existed and was updated successfully
Row 530: User (username=Michelle.Szymanski@superiorhealthplan.com, ID=1133) already existed and was updated successfully
Row 531: User (username=jared.wolfe@superiorhealthplan.com, ID=1134) already existed and was updated successfully
Row 532: User (username=mark.sanders@superiorhealthplan.com, ID=1135) already existed and was updated successfully
Row 533: User (username=karen.cheng@superiorhealthplan.com, ID=1136) already existed and was updated successfully
Row 534: User (username=chuck.hopson@superiorhealthplan.com, ID=1137) already existed and was updated successfully
Row 535: User (username=eric.glenn@superiorhealthplan.com, ID=1138) already existed and was updated successfully
Row 536: User (username=drew@lawsonstrategies.com, ID=1139) already existed and was updated successfully
Row 537: User (username=casey@blakemore.us, ID=1140) already existed and was updated successfully
Row 538: User (username=eddie@luciolegal.com, ID=1141) already existed and was updated successfully
Row 539: User (username=Billy@billyphenix.com, ID=1142) already existed and was updated successfully
Row 540: User (username=Will@billyphenix.com, ID=1143) already existed and was updated successfully
Row 541: User (username=revcobob@gmail.com, ID=1144) already existed and was updated successfully
Row 542: User (username=keith@bnsfirm.com, ID=1145) already existed and was updated successfully
Row 543: User (username=meason@tahp.org, ID=1147) already existed and was updated successfully
Row 544: User (username=kjones@taihooncology.com, ID=1148) already existed and was updated successfully
Row 545: User (username=lisa@daviskaufman.com, ID=1149) already existed and was updated successfully
Row 546: User (username=denise@daviskaufman.com, ID=1150) already existed and was updated successfully
Row 547: User (username=wendy@daviskaufman.com, ID=1151) already existed and was updated successfully
Row 548: User (username=jill.melton@tachp.org, ID=1152) already existed and was updated successfully
Row 549: User (username=rose@rahconsulting.com, ID=1153) already existed and was updated successfully
Row 550: User (username=kay.ghahremani@tachp.org, ID=1154) already existed and was updated successfully
Row 551: User (username=eawillia@texaschildrens.org, ID=1155) already existed and was updated successfully
Row 552: User (username=pcpeter@texaschildrens.org, ID=1156) already existed and was updated successfully
Row 553: User (username=pmhsing@texaschildrens.org, ID=1157) already existed and was updated successfully
Row 554: User (username=ebalvara@texaschildrens.org, ID=1158) already existed and was updated successfully
Row 555: User (username=mwmullar@texaschildrens.org, ID=1159) already existed and was updated successfully
Row 556: User (username=bsbabber@texaschildrens.org, ID=1160) already existed and was updated successfully
Row 557: User (username=kdbutler@texaschildrens.org, ID=1161) already existed and was updated successfully
Row 558: User (username=kkosterm@texaschildrens.org, ID=1162) already existed and was updated successfully
Row 559: User (username=cmhicks@texaschildrens.org, ID=1163) already existed and was updated successfully
Row 560: User (username=dhscardi@texaschildrens.org, ID=1164) already existed and was updated successfully
Row 561: User (username=tmdewey@texaschildrens.org, ID=1165) already existed and was updated successfully
Row 562: User (username=agsimms@texaschildrens.org, ID=1166) already existed and was updated successfully
Row 563: User (username=vawoznia@texaschildrens.org, ID=1167) already existed and was updated successfully
Row 564: User (username=smkim1@texaschildrens.org, ID=1168) already existed and was updated successfully
Row 565: User (username=vkparson@texaschildrens.org, ID=1169) already existed and was updated successfully
Row 566: User (username=jjingram@texaschildrens.org, ID=1170) already existed and was updated successfully
Row 567: User (username=bdlee@texaschildrens.org, ID=1171) already existed and was updated successfully
Row 568: User (username=txbarne1@texaschildrens.org, ID=1172) already existed and was updated successfully
Row 569: User (username=egcolvin@texaschildrens.org, ID=1173) already existed and was updated successfully
Row 570: User (username=aebriley@texaschildrens.org, ID=1174) already existed and was updated successfully
Row 571: User (username=KALEMMER@texaschildrens.org, ID=1175) already existed and was updated successfully
Row 572: User (username=snalliso@texaschildrens.org, ID=1176) already existed and was updated successfully
Row 573: User (username=axleeper@texaschildrens.org, ID=1177) already existed and was updated successfully
Row 574: User (username=jxbritto@texaschildrens.org, ID=1178) already existed and was updated successfully
Row 575: User (username=mhhill@texaschildrens.org, ID=1179) already existed and was updated successfully
Row 576: User (username=onwagner@texaschildrens.org, ID=1180) already existed and was updated successfully
Row 577: User (username=rxfleisc@texaschildrens.org, ID=1181) already existed and was updated successfully
Row 578: User (username=mxmurph4@texaschildrens.org, ID=1182) already existed and was updated successfully
Row 579: User (username=kehill1@texaschildrens.org, ID=1183) already existed and was updated successfully
Row 580: User (username=mrcooke@texaschildrens.org, ID=1184) already existed and was updated successfully
Row 581: User (username=jlcarls1@texaschildrens.org, ID=1185) already existed and was updated successfully
Row 582: User (username=smsmithe@texaschildrens.org, ID=1186) already existed and was updated successfully
Row 583: User (username=asriggs@texaschildrens.org, ID=1187) already existed and was updated successfully
Row 584: User (username=jnorton@texasmutual.com, ID=1188) already existed and was updated successfully
Row 585: User (username=paulschlaud@texasmutual.com, ID=1189) already existed and was updated successfully
Row 586: User (username=KWirsig@txmholdings.com, ID=1190) already existed and was updated successfully
Row 587: User (username=MDuncan@txmholdings.com, ID=1191) already existed and was updated successfully
Row 588: User (username=chad@texasstaralliance.com, ID=1192) already existed and was updated successfully
Row 589: User (username=ryan@texasstaralliance.com, ID=1193) already existed and was updated successfully
Row 590: User (username=lucinda@texasstaralliance.com, ID=1194) already existed and was updated successfully
Row 591: User (username=annie.nabers@thsa.org, ID=1195) already existed and was updated successfully
Row 592: User (username=george.gooch@thsa.org, ID=1196) already existed and was updated successfully
Row 593: User (username=eric.heflin@thsa.org, ID=1197) already existed and was updated successfully
Row 594: User (username=sarah@treatyoakstrategies.com, ID=1198) already existed and was updated successfully
Row 595: User (username=laurie@treatyoakstrategies.com, ID=1199) already existed and was updated successfully
Row 596: User (username=heather.durst@ucb.com, ID=1200) already existed and was updated successfully
Row 597: User (username=hope.berry@ucb.com, ID=1201) already existed and was updated successfully
Row 598: User (username=amy.whited@ucb.com, ID=1202) already existed and was updated successfully
Row 599: User (username=dfick@uhc.com, ID=1203) already existed and was updated successfully
Row 600: User (username=ankit.amin@uhc.com, ID=1204) already existed and was updated successfully
Row 601: User (username=jillian_hamblin@uhc.com, ID=1205) already existed and was updated successfully
Row 602: User (username=deborah_l_bond@uhc.com, ID=1206) already existed and was updated successfully
Row 603: User (username=patricia_logan@uhc.com, ID=1207) already existed and was updated successfully
Row 604: User (username=michelle.c.miller@uhc.com, ID=1208) already existed and was updated successfully
Row 605: User (username=angel.encinas@uhc.com, ID=1209) already existed and was updated successfully
Row 606: User (username=lsalcedo@uhc.com, ID=1210) already existed and was updated successfully
Row 607: User (username=mary_e_voysest@uhc.com, ID=1211) already existed and was updated successfully
Row 608: User (username=kelly_j_risch@uhc.com, ID=1212) already existed and was updated successfully
Row 609: User (username=zena.oshiro@uhc.com, ID=1213) already existed and was updated successfully
Row 610: User (username=mguillory@umojasupply.com, ID=1214) already existed and was updated successfully
Row 611: User (username=holly_hannes@uhc.com, ID=1215) already existed and was updated successfully
Row 612: User (username=davidsolyom@uhc.com, ID=1216) already existed and was updated successfully
Row 613: User (username=nmeier@uhc.com, ID=1217) already existed and was updated successfully
Row 614: User (username=johnathan_leonard@uhc.com, ID=1218) already existed and was updated successfully
Row 615: User (username=judi_shaw-rice@uhc.com, ID=1219) already existed and was updated successfully
Row 616: User (username=jazmin_elizondo@uhc.com, ID=1220) already existed and was updated successfully
Row 617: User (username=maria_g_shydlo@uhc.com, ID=1221) already existed and was updated successfully
Row 618: User (username=jeanne_m_cavanaugh@uhc.com, ID=1222) already existed and was updated successfully
Row 619: User (username=ginger_l_wommack@uhc.com, ID=1223) already existed and was updated successfully
Row 620: User (username=stephanie_n_vanarsdale@uhc.com, ID=1224) already existed and was updated successfully
Row 621: User (username=glenda_l_coleman@uhc.com, ID=1225) already existed and was updated successfully
Row 622: User (username=lara@txlobby.com, ID=1226) already existed and was updated successfully
Row 623: User (username=tiffany_handshy@uhc.com, ID=1227) already existed and was updated successfully
Row 624: User (username=desiree.melching@uhc.com, ID=1228) already existed and was updated successfully
Row 625: User (username=kristie_l_walker@uhc.com, ID=1229) already existed and was updated successfully
Row 626: User (username=arnita_burton@uhc.com, ID=1230) already existed and was updated successfully
Row 627: User (username=ellen.obrien@uhc.com, ID=1231) already existed and was updated successfully
Row 628: User (username=tamika_l_nolen@uhc.com, ID=1232) already existed and was updated successfully
Row 629: User (username=sdeshpande@uhc.com, ID=1233) already existed and was updated successfully
Row 630: User (username=kirk.zihlman@uhc.com, ID=1234) already existed and was updated successfully
Row 631: User (username=jeffrey.rayl@uhc.com, ID=1235) already existed and was updated successfully
Row 632: User (username=eyitoyosi_akuchie@uhc.com, ID=1236) already existed and was updated successfully
Row 633: User (username=david_k_hill@uhc.com, ID=1237) already existed and was updated successfully
Row 634: User (username=tracy.okolo@uhc.com, ID=1238) already existed and was updated successfully
Row 635: User (username=tanya.a.roberts@uhc.com, ID=1239) already existed and was updated successfully
Row 636: User (username=julie_b_garcia@uhc.com, ID=1240) already existed and was updated successfully
Row 637: User (username=ginna_wilson@uhc.com, ID=1241) already existed and was updated successfully
Row 638: User (username=mei_ling_christopher@uhc.com, ID=1242) already existed and was updated successfully
Row 639: User (username=meka_n_lasalle@uhc.com, ID=1243) already existed and was updated successfully
Row 640: User (username=joe_bedford@uhc.com, ID=1244) already existed and was updated successfully
Row 641: User (username=john_c_guedry@uhc.com, ID=1245) already existed and was updated successfully
Row 642: User (username=lcalo@uhc.com, ID=1246) already existed and was updated successfully
Row 643: User (username=angela_l_young@uhc.com, ID=1247) already existed and was updated successfully
Row 644: User (username=lisa_k_reuter@uhc.com, ID=1248) already existed and was updated successfully
Row 645: User (username=joe_trevino@uhc.com, ID=1249) already existed and was updated successfully
Row 646: User (username=juan_c_osorio@uhc.com, ID=1250) already existed and was updated successfully
Row 647: User (username=gena_r_jongebloed@uhc.com, ID=1251) already existed and was updated successfully
Row 648: User (username=megan_haddock@uhc.com, ID=1252) already existed and was updated successfully
Row 649: User (username=erica@epsconsulting.net, ID=1253) already existed and was updated successfully
Row 650: User (username=jeri_applegate@uhc.com, ID=1254) already existed and was updated successfully
Row 651: User (username=mary.l.henry-zeek@uhc.com, ID=1255) already existed and was updated successfully
Row 652: User (username=kristina.suberbielle@uhc.com, ID=1256) already existed and was updated successfully
Row 653: User (username=angela_trahan@uhc.com, ID=1257) already existed and was updated successfully
Row 654: User (username=yvette_r_wolfe@uhc.com, ID=1258) already existed and was updated successfully
Row 655: User (username=deborah_l_deska@uhc.com, ID=1259) already existed and was updated successfully
Row 656: User (username=sharmae_m_erickson@uhc.com, ID=1260) already existed and was updated successfully
Row 657: User (username=morgan.k.galow@uhc.com, ID=1261) already existed and was updated successfully
Row 658: User (username=rachana_patwa@uhc.com, ID=1262) already existed and was updated successfully
Row 659: User (username=david_milich@uhc.com, ID=1263) already existed and was updated successfully
Row 660: User (username=christina_murphy@uhc.com, ID=1264) already existed and was updated successfully
Row 661: User (username=christi_wondrash@uhc.com, ID=1265) already existed and was updated successfully
Row 662: User (username=maria_d_moreland@uhc.com, ID=1266) already existed and was updated successfully
Row 663: User (username=patricia_l_cobb@uhc.com, ID=1267) already existed and was updated successfully
Row 664: User (username=lauren_a_caddell@uhc.com, ID=1268) already existed and was updated successfully
Row 665: User (username=mandie.eichenlaub@uhc.com, ID=1269) already existed and was updated successfully
Row 666: User (username=marshall_dawer@uhc.com, ID=1270) already existed and was updated successfully
Row 667: User (username=kimberly_campbell@uhc.com, ID=1271) already existed and was updated successfully
Row 668: User (username=stephanie_villarreal@uhc.com, ID=1272) already existed and was updated successfully
Row 669: User (username=karen_howard@uhc.com, ID=1273) already existed and was updated successfully
Row 670: User (username=tammie_l_rogers@uhc.com, ID=1274) already existed and was updated successfully
Row 671: User (username=otaresiri_l_inije@uhc.com, ID=1275) already existed and was updated successfully
Row 672: User (username=srverratti@uhc.com, ID=1276) already existed and was updated successfully
Row 673: User (username=elizabeth_lamair@uhc.com, ID=1277) already existed and was updated successfully
Row 674: User (username=lindsey_farley@uhc.com, ID=1278) already existed and was updated successfully
Row 675: User (username=caitlyn.maccollum@uhc.com, ID=1279) already existed and was updated successfully
Row 676: User (username=sonal_shah@uhc.com, ID=1280) already existed and was updated successfully
Row 677: User (username=kristie_k_young@uhc.com, ID=1281) already existed and was updated successfully
Row 678: User (username=bobbie_j_salinas@uhc.com, ID=1282) already existed and was updated successfully
Row 679: User (username=alison_f_garton@uhc.com, ID=1283) already existed and was updated successfully
Row 680: User (username=Jenniferrodriguez@me.com, ID=1284) already existed and was updated successfully
Row 681: User (username=marc@marctx.com, ID=1285) already existed and was updated successfully
Row 682: User (username=chrisrtraylor@gmail.com, ID=1286) already existed and was updated successfully
Row 683: User (username=linda.l.baker@uhc.com, ID=1287) already existed and was updated successfully
Row 684: User (username=mary_h_beery@uhc.com, ID=1288) already existed and was updated successfully
Row 685: User (username=brandy@brandymarquez.com, ID=1289) already existed and was updated successfully
Row 686: User (username=karla_mione@uhc.com, ID=1290) already existed and was updated successfully
Row 687: User (username=gregg_sherrill@uhc.com, ID=1291) already existed and was updated successfully
Row 688: User (username=caren_zysk@uhc.com, ID=1292) already existed and was updated successfully
Row 689: User (username=susan_brunes@uhc.com, ID=1293) already existed and was updated successfully
Row 690: User (username=shauna_ewing@uhc.com, ID=1294) already existed and was updated successfully
Row 691: User (username=diane_kochol@uhc.com, ID=1295) already existed and was updated successfully
Row 692: User (username=Susan_Brunes@uhc.com, ID=1293) already existed and was updated successfully
Row 693: User (username=jeffrey_maddox@uhc.com, ID=1296) already existed and was updated successfully
Row 694: User (username=scott_flannery@uhc.com, ID=1297) already existed and was updated successfully
Row 695: User (username=chris_cronn@uhg.com, ID=1298) already existed and was updated successfully
Row 696: User (username=marian_cabanillas@uhc.com, ID=1299) already existed and was updated successfully
Row 697: User (username=don_langer@uhc.com, ID=1300) already existed and was updated successfully
Row 698: User (username=patricia_camacho-longoria@uhc.com, ID=1301) already existed and was updated successfully
Row 699: User (username=bernie_inskeep@uhc.com, ID=1302) already existed and was updated successfully
Row 700: User (username=brett_m_edwards@uhc.com, ID=1303) already existed and was updated successfully
Row 701: User (username=alisa.lotrakul@uhc.com, ID=1304) already existed and was updated successfully
Row 702: User (username=addover@usablemutual.com, ID=1305) already existed and was updated successfully
Row 703: User (username=tggauger@usablemutual.com, ID=1306) already existed and was updated successfully
Row 704: User (username=dwfrazier@arkbluecross.com, ID=1307) already existed and was updated successfully
Row 705: User (username=mrmartin@arkbluecross.com, ID=1308) already existed and was updated successfully
Row 706: User (username=vkwoods@arkbluecross.com, ID=1309) already existed and was updated successfully
Row 707: User (username=bkdorathy@arkbluecross.com, ID=1310) already existed and was updated successfully
Row 708: User (username=cebarnett@arkbluecross.com, ID=1311) already existed and was updated successfully
Row 709: User (username=zachrisman@usablemutual.com, ID=1312) already existed and was updated successfully
Row 710: User (username=majames@arkbluecross.com, ID=1313) already existed and was updated successfully
Row 711: User (username=skstanley@usablemutual.com, ID=1314) already existed and was updated successfully
Row 712: User (username=jdtreece@arkbluecross.com, ID=1315) already existed and was updated successfully
Row 713: User (username=mcdodson@usablemutual.com, ID=1316) already existed and was updated successfully
Row 714: User (username=aecates@arkbluecross.com, ID=1317) already existed and was updated successfully
Row 715: User (username=fbsewall@usablemutual.com, ID=1318) already existed and was updated successfully
Row 716: User (username=cmkittler@usablemutual.com, ID=1319) already existed and was updated successfully
Row 717: User (username=srobinson@valuehealth.com, ID=1320) already existed and was updated successfully
Row 718: User (username=tmattingly@valuehealth.com, ID=1321) already existed and was updated successfully
Row 719: User (username=rfowle@valuehealth.com, ID=1322) already existed and was updated successfully
Row 720: User (username=david.dunbar@versanthealth.com, ID=1323) already existed and was updated successfully
Row 721: User (username=megan.ryczek@versanthealth.com, ID=1324) already existed and was updated successfully
Row 722: User (username=courtney.jonesduggan@versanthealth.com, ID=1325) already existed and was updated successfully
Row 723: User (username=lisa.olexy@versanthealth.com, ID=1326) already existed and was updated successfully
Row 724: User (username=vaughn.koter@versanthealth.com, ID=1327) already existed and was updated successfully
Row 725: User (username=Danielle.Angel@versanthealth.com, ID=1328) already existed and was updated successfully
Row 726: User (username=beth.rossi@wildbluehealthsolutions.com, ID=1329) already existed and was updated successfully
Row 727: User (username=ken.janda@wildbluehealthsolutions.com, ID=1330) already existed and was updated successfully
Row 728: User (username=daniel.crowe@wildbluehealthsolutions.com, ID=1331) already existed and was updated successfully
Row 729: User (username=bcatano@winstead.com, ID=1332) already existed and was updated successfully
Row 730: User (username=aharvey@winstead.com, ID=1333) already existed and was updated successfully
Row 731: User (username=crupprath@winstead.com, ID=1334) already existed and was updated successfully
Row 732: User (username=jloehr@winstead.com, ID=1335) already existed and was updated successfully
Row 733: User (username=gorr@zeomega.com, ID=1336) already existed and was updated successfully
Row 734: User (username=mhopper@zeomega.com, ID=1337) already existed and was updated successfully
Row 735: User (username=shameet@vheda.com, ID=1338) already existed and was updated successfully
Row 736: User (username=david.williams@podimetrics.com, ID=1339) already existed and was updated successfully
Row 737: User (username=lori.howarth@bayer.com, ID=1340) already existed and was updated successfully
Row 738: User (username=cindy.buckels@rightsitehealth.com, ID=1341) already existed and was updated successfully
Row 739: User (username=edalexander@goodrootinc.com, ID=1342) already existed and was updated successfully
Row 740: User (username=rcipriano@scene.health, ID=1343) already existed and was updated successfully
Row 741: User (username=blovely@hhaexchange.com, ID=1344) already existed and was updated successfully
Row 742: User (username=smcleod@itilitiheatlh.com, ID=1345) already existed and was updated successfully
Row 743: User (username=payal.parekh@phhs.org, ID=1346) already existed and was updated successfully
Row 744: User (username=j_allison_grant@uhc.com, ID=1347) already existed and was updated successfully
Row 745: User (username=jennifer_a_saenz@uhc.com, ID=1348) already existed and was updated successfully
Row 746: User (username=Adelaida.Corral@alivi.com, ID=60) already existed and was updated successfully
Row 747: User (username=dstreeter@caqh.org, ID=1349) already existed and was updated successfully
Row 748: User (username=caroline.seeley@carebridgehealth.com, ID=1350) already existed and was updated successfully
Row 749: User (username=cassandra.mendenhall@organon.com, ID=1351) already existed and was updated successfully
Row 750: User (username=katherina.tinney@organon.com, ID=1352) already existed and was updated successfully
Row 751: User (username=lisa.davis2@organon.com, ID=1353) already existed and was updated successfully
Row 752: User (username=adelaida.corral@alivi.com, ID=60) already existed and was updated successfully
Row 753: User (username=johnathan.gallop@superiorhealthplan.com, ID=1354) already existed and was updated successfully
Row 754: User (username=nathan.hoover@superiorhealthplan.com, ID=1130) already existed and was updated successfully
Row 755: User (username=shari_waldie@bcbstx.com, ID=193) already existed and was updated successfully
Row 756: User (username=jason.gajewski@superiorhealthplan.com, ID=70) already existed and was updated successfully
Row 757: User (username=cheryl.d.rhines@superiorhealthplan.com, ID=71) already existed and was updated successfully
Row 758: User (username=jennifer.houston@superiorhealthplan.com, ID=73) already existed and was updated successfully
Row 759: User (username=maria.elizarde@superiorhealthplan.com, ID=75) already existed and was updated successfully
Row 760: User (username=leticia.espiritu@superiorhealthplan.com, ID=76) already existed and was updated successfully
Row 761: User (username=twinn@superiorhealthplan.com, ID=77) already existed and was updated successfully
Row 762: User (username=Dominic.Weilbaecher@babsondx.com, ID=85) already existed and was updated successfully
Row 763: User (username=chuck.grabow@superiorhealthplan.com, ID=1355) already existed and was updated successfully
Row 764: User (username=Tessa.Perez@dchstx.org, ID=1356) already existed and was updated successfully
Row 765: User (username=alex.sommer@avalonhcs.com, ID=127) already existed and was updated successfully
Row 766: User (username=joel.meyer@novartis.com, ID=1357) already existed and was updated successfully
Row 767: User (username=christy.gustafson@superiorhealthplan.com, ID=1358) already existed and was updated successfully
Row 768: User (username=brad.clay@novartis.com, ID=1359) already existed and was updated successfully
Row 769: User (username=alan.picard@novartis.com, ID=1360) already existed and was updated successfully
Row 770: User (username=mai.duong@novartis.com, ID=1361) already existed and was updated successfully
Row 771: User (username=melissa.deep@emcarahealth.com, ID=1362) already existed and was updated successfully
Row 772: User (username=Heather_R_Martinez@bcbstx.com, ID=194) already existed and was updated successfully
Row 773: User (username=mcostello@dsswtx.org, ID=1363) already existed and was updated successfully
Row 774: User (username=kjeffrey@cdsintexas.com, ID=1364) already existed and was updated successfully
Row 775: User (username=abaker@cdsintexas.com, ID=1365) already existed and was updated successfully
Row 776: User (username=lnbaker@cdsintexas.com, ID=1366) already existed and was updated successfully
Row 777: User (username=KIMBERLY.AARON@COOKCHILDRENS.ORG, ID=91) already existed and was updated successfully
Row 778: User (username=Teresa.gonzales@superiorhealthplan.com, ID=1128) already existed and was updated successfully
Row 779: User (username=nikki.lobdell@cookchildrens.org, ID=1367) already existed and was updated successfully
Row 780: User (username=heather.korbulic@getinsured.com, ID=1368) already existed and was updated successfully
Row 781: User (username=paul.neutz@getinsured.com, ID=1369) already existed and was updated successfully
Row 782: User (username=lauraslawlor@gmail.com, ID=1370) already existed and was updated successfully
Row 783: User (username=julia.figueroa2@superiorhealthplan.com, ID=1371) already existed and was updated successfully
Row 784: User (username=testuser@tester.com, ID=98) already existed and was updated successfully
Row 785: User (username=testnewsuserfast@test.com, ID=99) already existed and was updated successfully
Row 786: User (username=Bergan00@gmail.com, ID=100) already existed and was updated successfully
Row 787: User (username=CMHicks@texaschildrens.org, ID=1163) already existed and was updated successfully
Row 788: User (username=kxscottg@texaschildrens.org, ID=1372) already existed and was updated successfully
Row 789: User (username=eeanders@texaschildrens.org, ID=1373) already existed and was updated successfully
Row 790: User (username=lrfulle1@texaschildrens.org, ID=1374) already existed and was updated successfully
Row 791: User (username=Lauren.Rios@dchstx.org, ID=1375) already existed and was updated successfully
Row 792: User (username=Marcy.dickson@molinahealthcare.com, ID=730) already existed and was updated successfully
Row 793: User (username=Elaine_Gold@bcbsil.com, ID=182) already existed and was updated successfully
Row 794: User (username=leetagreer@gmail.com, ID=1376) already existed and was updated successfully
Row 795: User (username=Rebecca.Solis@molinahealthcare.com, ID=1377) already existed and was updated successfully
Row 796: User (username=robin.reimschissel@molinahealthcare.com, ID=1378) already existed and was updated successfully
Row 797: User (username=edna.dudley@molinahealthcare.com, ID=1379) already existed and was updated successfully
Row 798: User (username=rachel.hopkins@molinahealthcare.com, ID=1380) already existed and was updated successfully
Row 799: User (username=Maria.Guerrero@Molinahealthcare.com, ID=1381) already existed and was updated successfully
Row 800: User (username=Stephen.Bush@BSWHealth.org, ID=1382) already existed and was updated successfully
Row 801: User (username=Suzanne_Lakin@bcbstx.com, ID=184) already existed and was updated successfully
Row 802: User (username=maren.peterson@uhc.com, ID=1383) already existed and was updated successfully
Row 803: User (username=wendy.mcgallion@molinahealthcare.come, ID=1384) already existed and was updated successfully
Row 804: User (username=cstephens@mcna.net, ID=1385) already existed and was updated successfully
Row 805: User (username=sharon.alvis@senderohealth.com, ID=1386) already existed and was updated successfully
Row 806: User (username=nicole@curative.com, ID=1387) already existed and was updated successfully
Row 807: User (username=madison.armbrester@carebridgehealth.com, ID=1388) already existed and was updated successfully
Row 808: User (username=sxsivert@texaschildrens.org, ID=1389) already existed and was updated successfully
Row 809: User (username=kari.suttee@novartis.com, ID=1390) already existed and was updated successfully
Row 810: User (username=neel.patel@phhs.org, ID=861) already existed and was updated successfully
Row 811: User (username=weylieb@aetna.com, ID=416) already existed and was updated successfully
Row 812: User (username=mayra_dominguez@uhc.com, ID=1391) already existed and was updated successfully
Row 813: User (username=sandi.howard@optum.com, ID=1392) already existed and was updated successfully
Row 814: User (username=Ankit_x_patel@bcbsil.com, ID=187) already existed and was updated successfully
Row 815: User (username=Mark.Shaffer@Molinahealthcare.com, ID=726) already existed and was updated successfully
Row 816: User (username=yford@cfhp.com, ID=1393) already existed and was updated successfully
Row 817: User (username=Teresa_Devine@bcbstx.com, ID=161) already existed and was updated successfully
Row 818: User (username=leticia.ontiveros@superiorhealthplan.com, ID=1394) already existed and was updated successfully
Row 819: User (username=arnulfo.ramirez@dchstx.org, ID=1395) already existed and was updated successfully
Row 820: User (username=DARWYN.WALKER@COOKCHILDRENS.ORG, ID=451) already existed and was updated successfully
Row 821: User (username=Veronica.LaDuc@superiorhealthplan.com, ID=1090) already existed and was updated successfully
Row 822: User (username=kandice.sanaie@cignahealthcare.com, ID=1396) already existed and was updated successfully
Row 823: User (username=amy.teske7@gmail.com, ID=1397) already existed and was updated successfully
Row 824: User (username=maneesh.roberts@cookchildrens.org, ID=1398) already existed and was updated successfully
Row 825: User (username=Felicia.Ramirez@phhs.org, ID=853) already existed and was updated successfully
Row 826: User (username=yahaira.perez@cookchildrens.org, ID=1399) already existed and was updated successfully
Row 827: User (username=Stephanie.Edwards@superiorhealthplan.com, ID=1400) already existed and was updated successfully
Row 828: User (username=Erica.lerma@elpasohealth.com, ID=580) already existed and was updated successfully
Row 829: User (username=jnorman@elpasohealth.com, ID=1401) already existed and was updated successfully
Row 830: User (username=rbarrozo@elpasohealth.com, ID=1402) already existed and was updated successfully
Row 831: User (username=andersonc7@aetna.com, ID=421) already existed and was updated successfully
Row 832: User (username=rebecca.stokes@Molinahealthcare.com, ID=716) already existed and was updated successfully
Row 833: User (username=Hochhaltera@aetna.com, ID=384) already existed and was updated successfully
Row 834: User (username=Barbara.stanley@superiorhealthplan.com, ID=1403) already existed and was updated successfully
Row 835: User (username=Robbin.Patton@cookchildrens.org, ID=436) already existed and was updated successfully
Row 836: User (username=nicole.gonzales2@molinahealthcare.com, ID=736) already existed and was updated successfully
Row 837: User (username=stacie.walkerposvar@bswhealth.org, ID=949) already existed and was updated successfully
Row 838: User (username=jasonleonwright@gmail.com, ID=1404) already existed and was updated successfully
Row 839: User (username=john.majors@bswhealth.org, ID=942) already existed and was updated successfully
Row 840: User (username=shyama.gandhi@molinahealthcare.com, ID=1405) already existed and was updated successfully
Row 841: User (username=jason.wright@phhs.org, ID=1406) already existed and was updated successfully
Row 842: User (username=christine.stivers@superiorhealthplan.com, ID=1407) already existed and was updated successfully
Row 843: User (username=dee_cavaness@bcbstx.com, ID=190) already existed and was updated successfully
Row 844: User (username=HarrisS16@aetna.com, ID=412) already existed and was updated successfully
Row 845: User (username=kandice_walker@bcbstx.com, ID=173) already existed and was updated successfully
Row 846: User (username=John_Sanchez@bcbstx.com, ID=179) already existed and was updated successfully
Row 847: User (username=kunal_parekh@bcbsil.com, ID=180) already existed and was updated successfully
Row 848: User (username=Janie_Park@bcbstx.com, ID=186) already existed and was updated successfully
Row 849: User (username=exvillaf@texaschildrens.org, ID=1408) already existed and was updated successfully
Row 850: User (username=cdominguez@elpasohealth.com, ID=1409) already existed and was updated successfully
Row 851: User (username=blesing_amazigo@uhc.com, ID=1410) already existed and was updated successfully
Row 852: User (username=akhil.raj@superiorhealthplan.com, ID=1411) already existed and was updated successfully
Row 853: User (username=patsy.vrazel@bswhealth.org, ID=956) already existed and was updated successfully
Row 854: User (username=jolynn@superhealthplan.com, ID=1412) already existed and was updated successfully
Row 855: User (username=thomas.moreland@superiorhealthplan.com, ID=1413) already existed and was updated successfully
Row 856: User (username=Sara.D.Yepez@superiorhealthplan.com, ID=1414) already existed and was updated successfully
Row 857: User (username=tam.donnelly@dchstx.org, ID=583) already existed and was updated successfully
Row 858: User (username=Nathan_Fortner@bcbstx.com, ID=192) already existed and was updated successfully
Row 859: User (username=jennifer_housley@bcbstx.com, ID=191) already existed and was updated successfully
Row 860: User (username=Xochil_zevallos@uhc.com, ID=1415) already existed and was updated successfully
Row 861: User (username=Sheila_Strode@bcbsil.com, ID=197) already existed and was updated successfully
Row 862: User (username=tracie.acosta@bswhealth.com, ID=1416) already existed and was updated successfully
Row 863: User (username=cristal.detert@bswhealth.org, ID=953) already existed and was updated successfully
Row 864: User (username=Christine.Williams@cookchildrens.org, ID=372) already existed and was updated successfully
Row 865: User (username=Martinj4@aetna.com, ID=400) already existed and was updated successfully
Row 866: User (username=angela.guerrero@dchstx.org, ID=1417) already existed and was updated successfully
Row 867: User (username=sabrina.heins@dchstx.org, ID=551) already existed and was updated successfully
Row 868: User (username=angela_moemeka@bcbstx.com, ID=172) already existed and was updated successfully
Row 869: User (username=ALLISON.HAYS@COOKCHILDRENS.ORG, ID=1418) already existed and was updated successfully
Row 870: User (username=jolene_bossier@bcbstx.com, ID=189) already existed and was updated successfully
Row 871: User (username=Angela.Smith@cookchildrens.org, ID=373) already existed and was updated successfully
Row 872: User (username=mvnguyen2@ascension.org, ID=1009) already existed and was updated successfully
Row 873: User (username=carrianne.dockter@molinahealthcare.com, ID=1419) already existed and was updated successfully
Row 874: User (username=kwwhatl1@texaschildrens.org, ID=1420) already existed and was updated successfully
Row 875: User (username=DL_CFHP_Regulatory@CFHP.com, ID=338) already existed and was updated successfully
Row 876: User (username=DL_Medicaid_TAHP_OPS@cfhp.com, ID=365) already existed and was updated successfully
Row 877: User (username=Carrianne.Dockter@MolinaHealthCare.com, ID=1419) already existed and was updated successfully
Row 878: User (username=brittany.hall@superiorhealthplan.com, ID=1421) already existed and was updated successfully
Row 879: User (username=marivera@centene.com, ID=1422) already existed and was updated successfully
Row 880: User (username=danita.steward@molinahealthcare.com, ID=733) already existed and was updated successfully
Row 881: User (username=sowndharya_sunder@bcbstx.com, ID=181) already existed and was updated successfully
Row 882: User (username=Araceli_Cappello@bcbstx.com, ID=183) already existed and was updated successfully
Row 883: User (username=dominic_garcia@bcbstx.com, ID=185) already existed and was updated successfully
Row 884: User (username=daimon.krumlauf@superiorhealthplan.com, ID=1423) already existed and was updated successfully
Row 885: User (username=mespinoza@elpasohealth.com, ID=1424) already existed and was updated successfully
Row 886: User (username=Hany.aziz@molinahealthcare.com, ID=704) already existed and was updated successfully
Row 887: User (username=victoria_cage@bcbstx.com, ID=188) already existed and was updated successfully
Row 888: User (username=elizabeth_lade@bcbstx.com, ID=195) already existed and was updated successfully
Row 889: User (username=plaso437@gmail.com, ID=101) already existed and was updated successfully
Row 890: User (username=Leeta.greer@molinahealthcare.com, ID=1425) already existed and was updated successfully
Row 891: User (username=Jessica.mendoza2@superiorhealthplan.com, ID=1426) already existed and was updated successfully
Row 892: User (username=kristy.bulhoes@bswhealth.org, ID=939) already existed and was updated successfully
Row 893: User (username=tara.stafford@bswhealth.org, ID=940) already existed and was updated successfully
Row 894: User (username=Laci.Noble@bswhealth.org, ID=951) already existed and was updated successfully
Row 895: User (username=lucy.chibesa@bswhealth.org, ID=1427) already existed and was updated successfully
Row 896: User (username=AXTESKE@TEXASCHILDRENS.ORG, ID=1428) already existed and was updated successfully
Row 897: User (username=wendy.richerson@BSWHealth.org, ID=1429) already existed and was updated successfully
Row 898: User (username=melissa.loper@bswhealth.org, ID=1430) already existed and was updated successfully
Row 899: User (username=marc.rains@cookchildrens.org, ID=1431) already existed and was updated successfully
Row 900: User (username=Chevalier_DeShay@bcbstx.com, ID=196) already existed and was updated successfully
Row 901: User (username=Lynn.Ramsey@dchstx.org, ID=1432) already existed and was updated successfully
Row 902: User (username=james.locke@molinahealthcare.com, ID=1433) already existed and was updated successfully
Row 903: User (username=jon.janovec@greatdentalplans.com, ID=1434) already existed and was updated successfully
Row 904: User (username=kevin.miller@dentaquest.com, ID=1435) already existed and was updated successfully
Row 905: User (username=mchapa@cfhp.com, ID=1436) already existed and was updated successfully
Row 906: User (username=angela_kaiser@bcbstx.com, ID=198) already existed and was updated successfully
Row 907: User (username=lisa.fillip@BSWHealth.org, ID=906) already existed and was updated successfully
Row 908: User (username=jserna@elpasohealth.com, ID=1437) already existed and was updated successfully
Row 909: User (username=courtney.mckevie@superiorhealthplan.com, ID=1438) already existed and was updated successfully
Row 910: User (username=Esther.Webb@BSWHealth.org, ID=958) already existed and was updated successfully
Row 911: User (username=lcrow@cfhp.com, ID=353) already existed and was updated successfully
Row 912: User (username=rkerr@elpasohealth.com, ID=1439) already existed and was updated successfully
Row 913: User (username=samuel.steinmetz@uhc.com, ID=1440) already existed and was updated successfully
Row 914: User (username=vera.martinez@cookchildrens.org, ID=1441) already existed and was updated successfully
Row 915: User (username=REBECCA.BELMONT@COOKCHILDRENS.ORG, ID=1442) already existed and was updated successfully
Row 916: User (username=jennifer.boreing@bswhealth.org, ID=938) already existed and was updated successfully
Row 917: User (username=Matt.Keppler@changehealthcare.com, ID=1443) already existed and was updated successfully

"""

# Second set of input data
input_text_2 = """
bob.clark@memorialhermann.org	bob.clark@memorialhermann.org	Bob	Clark	823	Health Plan Employee
gina.mackey@memorialhermann.org	gina.mackey@memorialhermann.org	Gina	Mackey	823	Health Plan Employee
annemarie.stakes@memorialhermann.org	annemarie.stakes@memorialhermann.org	Anne Marie	Stakes	823	Health Plan Employee
jacqueline.haggerty@memorialhermann.org	jacqueline.haggerty@memorialhermann.org	Jacqueline	Haggerty	823	Health Plan Employee
joi.mcclure@memorialhermann.org	joi.mcclure@memorialhermann.org	Joi	McClure	823	Health Plan Employee
buck.colomy@memorialhermann.org	buck.colomy@memorialhermann.org	Buck	Colomy	823	Health Plan Employee
david.martin2@memorialhermann.org	david.martin2@memorialhermann.org	David	Martin	823	Health Plan Employee
steve.soman@memorialhermann.org	steve.soman@memorialhermann.org	Steve	Soman	823	Health Plan Employee
Robert.Clark@memorialhermann.org	Robert.Clark@memorialhermann.org	Robert	Clark	823	Health Plan Employee
Stephanie.Osemwegie@memorialhermann.org	Stephanie.Osemwegie@memorialhermann.org	Stephanie	Osemwgie	823	Health Plan Employee
Tawanda.Wilson@memorialhermann.org	Tawanda.Wilson@memorialhermann.org	Tawanda	Wilson	823	Health Plan Employee
AnneMarie.Stakes@apex4health.com	AnneMarie.Stakes@apex4health.com	AnneMarie	Stakes	823	Health Plan Employee
Melony.young@apex4health.com	Melony.young@apex4health.com	Melony	Young	823	Health Plan Employee
Wintana.Harness@memorialhermann.org	Wintana.Harness@memorialhermann.org	Wintana	Harness	823	Health Plan Employee
jay.hurt2@memorialhermann.org	jay.hurt2@memorialhermann.org	Jay	Hurt	823	Health Plan Employee
Jay.Hurt@apex4health.com	Jay.Hurt@apex4health.com	Jay	Hurt	823	Health Plan Employee
holly.turner@merck.com	holly.turner@merck.com	Holly	Turner	819	Affiliate
grace.pelkowski@merck.com	grace.pelkowski@merck.com	Grace	Pelkowski	819	Affiliate
jennifer.melchior@milliman.com	jennifer.melchior@milliman.com	Jennifer	Melchior	819	Affiliate
fritz.busch@milliman.com	fritz.busch@milliman.com	FREDERICK	BUSCH	819	Affiliate
raleigh.skaggs@milliman.com	raleigh.skaggs@milliman.com	Raleigh	Skaggs	819	Affiliate
tim.lee@milliman.com	tim.lee@milliman.com	Tim	Lee	819	Affiliate
jeff.milton-hall@milliman.com	jeff.milton-hall@milliman.com	Jeff	Milton-Hall	819	Affiliate
jason.nowakowski@milliman.com	jason.nowakowski@milliman.com	Jason	Nowakowski	819	Affiliate
mary.creten@milliman.com	mary.creten@milliman.com	Mary	Creten	819	Affiliate
paul.houchens@milliman.com	paul.houchens@milliman.com	Paul	Houchens	819	Affiliate
bill.mckinley@milliman.com	bill.mckinley@milliman.com	Bill	McKinley	819	Affiliate
charlie.mills@milliman.com	charlie.mills@milliman.com	Charlie	Mills	819	Affiliate
darin.muse@milliman.com	darin.muse@milliman.com	Darin	Muse	819	Affiliate
ccliett@mwsgw.com	ccliett@mwsgw.com	Charles	Cliett	819	Professional Affiliate
bkitchin@mwlaw.com	bkitchin@mwlaw.com	Brytne	Kitchin	819	Professional Affiliate
sstrickland@mwlaw.com	sstrickland@mwlaw.com	Stanton	Strickland	819	Professional Affiliate
rtredway@mwlaw.com	rtredway@mwlaw.com	Ryan	Tredway	819	Professional Affiliate
rtredway@mwlaw.com	rtredway@mwlaw.com	Ryan	Tredway	823	Health Plan Contract Lobbyist
mnored@mwlaw.com	mnored@mwlaw.com	Michael	Nored	819	Professional Affiliate
james_datz@mt-pharma-us.com	james_datz@mt-pharma-us.com	James	Datz	819	Affiliate
william_gittinger@mt-pharma-us.com	william_gittinger@mt-pharma-us.com	william	gittinger	819	Affiliate
david_holman@mt-pharma-us.com	david_holman@mt-pharma-us.com	David	Holman	819	Affiliate
scott.white@modahealth.com	scott.white@modahealth.com	Scott	White	823	Health Plan Employee
addy.binkley@modahealth.com	addy.binkley@modahealth.com	Addy	Binkley	823	Health Plan Employee
Muriel.magee@modahealth.com	Muriel.magee@modahealth.com	Muriel	Magee	823	Health Plan Employee
James.light@modahealth.com	James.light@modahealth.com	James	Light	823	Health Plan Employee
Toni.ostrom@modahealth.com	Toni.ostrom@modahealth.com	Toni	Ostrom	823	Health Plan Employee
melisa.strong@modahealth.com	melisa.strong@modahealth.com	Melissa	Strong	823	Health Plan Employee
Suzannah.dellacorte@modahealth.com	Suzannah.dellacorte@modahealth.com	Suzannah	Dellacorte	823	Health Plan Employee
Yale.popowich@modahealth.com	Yale.popowich@modahealth.com	Yale	Popowich	823	Health Plan Employee
Katie.scheelar@modahealth.com	Katie.scheelar@modahealth.com	Katie	Scheelar	823	Health Plan Employee
Carly.rodriguez@modahealth.com	Carly.rodriguez@modahealth.com	Carly	Rodriguez	823	Health Plan Employee
Cole.ahnberg@modahealth.com	Cole.ahnberg@modahealth.com	Cole	Ahnberg	823	Health Plan Employee
Katie.brokaw@modahealth.com	Katie.brokaw@modahealth.com	Katie	Brokaw	823	Health Plan Employee
Jason.gootee@modahealth.com	Jason.gootee@modahealth.com	Jason	Gootee	823	Health Plan Employee
theresa.barney@modahealth.com	theresa.barney@modahealth.com	Theresa	Barney	823	Health Plan Employee
joe.greenman@modahealth.com	joe.greenman@modahealth.com	Joe	Greenman	823	Health Plan Employee
sean.jessup@modahealth.com	sean.jessup@modahealth.com	Sean	Jessup	823	Health Plan Employee
kayla.jones@modahealth.com	kayla.jones@modahealth.com	Kayla	Jones	823	Health Plan Employee
stevenf@modivcare.com	stevenf@modivcare.com	Steven	Fiest	819	Associate
dennis.halmai@modivcare.com	dennis.halmai@modivcare.com	Dennis	Halmai	819	Associate
david.heckel@modivcare.com	david.heckel@modivcare.com	David	Heckel	819	Associate
kathleen.payne@modivcare.com	kathleen.payne@modivcare.com	Kathleen	Payne	819	Associate
katherynn.fischer@logisticare.com	katherynn.fischer@logisticare.com	Katherynn	Fischer	819	Associate
phil.eades@modivcare.com	phil.eades@modivcare.com	Phil	Eades	819	Associate
brittany.haggstrom@modivcare.com	brittany.haggstrom@modivcare.com	Brittany	Haggstrom	819	Associate
michael.hankinson@modivcare.com	michael.hankinson@modivcare.com	Michael	Hankinson	819	Associate
carol.weil@molinahealthcare.com	carol.weil@molinahealthcare.com	Carol	Weil	823	Health Plan Employee
michelle.bentzien-purrington@molinahealthcare.com	michelle.bentzien-purrington@molinahealthcare.com	MIchelle	Bentzien-Purrington	823	Health Plan Employee
paul.sturm@molinahealthcare.com	paul.sturm@molinahealthcare.com	Paul	Sturm	823	Health Plan Employee
maharlika.delpilar@molinahealthcare.com	maharlika.delpilar@molinahealthcare.com	Maharilika	Delpilar	823	Health Plan Employee
cynthia.diaz1@molinahealthcare.com	cynthia.diaz1@molinahealthcare.com	Cynthia	Diaz	823	Health Plan Employee
cameron.smyth@molinahealthcare.com	cameron.smyth@molinahealthcare.com	Cameron	Smyth	823	Health Plan Employee
kate.koons@molinahealthcare.com	kate.koons@molinahealthcare.com	Kate	Koons	823	Health Plan Employee
david.valdez1@molinahealthcare.com	david.valdez1@molinahealthcare.com	David	Valdez	823	Health Plan Employee
jim.locke@molinahealthcare.com	jim.locke@molinahealthcare.com	Jim	Locke	823	Health Plan Employee
gretchen.schuleman@molinahealthcare.com	gretchen.schuleman@molinahealthcare.com	Gretchen	Schuleman	823	Health Plan Employee
emran.rouf@molinahealthcare.com	emran.rouf@molinahealthcare.com	Emran	Rouf	823	Health Plan Employee
barbara.bagley@molinahealthcare.com	barbara.bagley@molinahealthcare.com	Barbara	Bagley	823	Health Plan Employee
hany.aziz@molinahealthcare.com	hany.aziz@molinahealthcare.com	Hany	Aziz	823	Health Plan Employee
naomi.alvarez@molinahealthcare.com	naomi.alvarez@molinahealthcare.com	Naomi	Alvarez	823	Health Plan Employee
joseph.vazhappilly@molinahealthcare.com	joseph.vazhappilly@molinahealthcare.com	Joseph	Vazhappilly	823	Health Plan Employee
carol.dobosh@molinahealthcare.com	carol.dobosh@molinahealthcare.com	Carol	Dobosh	823	Health Plan Employee
leticia.ramirez@molinahealthcare.com	leticia.ramirez@molinahealthcare.com	Leticia	Ramirez	823	Health Plan Employee
william.brendel@molinahealthcare.com	william.brendel@molinahealthcare.com	William	Brendel	823	Health Plan Employee
cindy.fortress@molinahealthcare.com	cindy.fortress@molinahealthcare.com	Cindy	Fortress	823	Health Plan Employee
brandie.gasper@molinahealthcare.com	brandie.gasper@molinahealthcare.com	Brandie	Gasper	823	Health Plan Employee
robert.kalin@molinahealthcare.com	robert.kalin@molinahealthcare.com	Robert	Kalin	823	Health Plan Employee
caren.zysk@molinahealthcare.com	caren.zysk@molinahealthcare.com	Caren	Zysk	823	Health Plan Employee
brandi.mcmillan@molinahealthcare.com	brandi.mcmillan@molinahealthcare.com	Brandi	McMillan	823	Health Plan Employee
audrey.terry@molinahealthcare.com	audrey.terry@molinahealthcare.com	Audrey	Terry	823	Health Plan Employee
deliverytx@molinahealthcare.com	deliverytx@molinahealthcare.com	Delivery	Molina	823	Health Plan Employee
gwendolyn.sowa@molinahealthcare.com	gwendolyn.sowa@molinahealthcare.com	Gwendolyn	Sowa	823	Health Plan Employee
rebecca.stokes@molinahealthcare.com	rebecca.stokes@molinahealthcare.com	Rebecca	Stokes	823	Health Plan Employee
caitlin.hogge2@molinahealthcare.com	caitlin.hogge2@molinahealthcare.com	Caitlin	Hogge	823	Health Plan Employee
marie.dinh@molinahealthcare.com	marie.dinh@molinahealthcare.com	Marie	Dinh	823	Health Plan Employee
kathryn.chapman@molinahealthcare.com	kathryn.chapman@molinahealthcare.com	Kathryn	Chapman	823	Health Plan Employee
jeffrey.stone@molinahealthcare.com	jeffrey.stone@molinahealthcare.com	Jeff	Stone	823	Health Plan Employee
programmanagementhcs@molinahealthcare.com	programmanagementhcs@molinahealthcare.com	Program	Management	823	Health Plan Employee
lauren.sorokolit@molinahealthcare.com	lauren.sorokolit@molinahealthcare.com	Lauren	Sorokolit	823	Health Plan Employee
shirley.bonney@molinahealthcare.com	shirley.bonney@molinahealthcare.com	Shirley	Bonney	823	Health Plan Employee
misha.lehman@molinahealthcare.com	misha.lehman@molinahealthcare.com	Misha	Lehman	823	Health Plan Employee
rachel.poe@molinahealthcare.com	rachel.poe@molinahealthcare.com	Rachel	Poe	823	Health Plan Employee
mark.shaffer@molinahealthcare.com	mark.shaffer@molinahealthcare.com	Mark 	Shaffer	823	Health Plan Employee
Wendy.McGallion@molinahealthcare.com	Wendy.McGallion@molinahealthcare.com	Wendy	McGallion	823	Health Plan Employee
Denise.Arvia@molinahealthcare.com	Denise.Arvia@molinahealthcare.com	Denise	Arvia	823	Health Plan Employee
Mary.singer@molinahealthcare.com	Mary.singer@molinahealthcare.com	Mary	Singer	823	Health Plan Employee
Marcy.Dickson@molinahealthcare.com	Marcy.Dickson@molinahealthcare.com	Marcy	Dickson	823	Health Plan Employee
Scott.albosta@molinahealthcare.com	Scott.albosta@molinahealthcare.com	Scott	Albosta	823	Health Plan Employee
Kelsey.Letcher@molinahealthcare.com	Kelsey.Letcher@molinahealthcare.com			823	Health Plan Employee
Rebecca.stokes@molinahealthcare.com	Rebecca.stokes@molinahealthcare.com	Rebecca	Stokes	823	Health Plan Employee
Danita.Steward@molinahealthcare.com	Danita.Steward@molinahealthcare.com			823	Health Plan Employee
Loretta.Smith@molinahealthcare.com	Loretta.Smith@molinahealthcare.com	Loretta	Smith	823	Health Plan Employee
susan.weinfurther@molinahealthcare.com	susan.weinfurther@molinahealthcare.com	Sue	Weinfurther	823	Health Plan Employee
Nicole.Gonzales2@MolinaHealthCare.Com	Nicole.Gonzales2@MolinaHealthCare.Com	Nicole	Gonzales	823	Health Plan Employee
Susan.Weinfurther@molinahealthcare.com	Susan.Weinfurther@molinahealthcare.com	Susan	Weinfurther	823	Health Plan Employee
rosario.groomes@molinahealthcare.com	rosario.groomes@molinahealthcare.com	Rosario	Groomes	823	Health Plan Employee
susan.herndon@molinahealthcare.com	susan.herndon@molinahealthcare.com	Susan	Herndon	823	Health Plan Employee
julia.hamilton@molinahealthcare.com	julia.hamilton@molinahealthcare.com	Julia	Hamilton	823	Health Plan Employee
lindsey.vasquez@molinahealthcare.com	lindsey.vasquez@molinahealthcare.com	Lindsey	Vasquez	823	Health Plan Employee
jimmy.pan@molinahealthcare.com	jimmy.pan@molinahealthcare.com	Jimmy	Pan	823	Health Plan Employee
chris.coffey@molinahealthcare.com	chris.coffey@molinahealthcare.com	Chris	Coffey	823	Health Plan Employee
kelsey.letcher@molinahealthcare.com	kelsey.letcher@molinahealthcare.com	Kelsey	Letcher	823	Health Plan Employee
tania.colon@molinahealthcare.com	tania.colon@molinahealthcare.com	Tania 	Colon	823	Health Plan Employee
bruce.lane@molinahealthcare.com	bruce.lane@molinahealthcare.com	Bruce	Lane	823	Health Plan Employee
mark.waggoner@momsmeals.com	mark.waggoner@momsmeals.com	Mark	Waggoner	819	Affiliate
michaella.johnson@mossadams.com	michaella.johnson@mossadams.com	Michaella	Johnson	819	Professional Affiliate
Brian.Conner@mossadams.com	Brian.Conner@mossadams.com	Brian	Conner	819	Professional Affiliate
Rachel.Laureno@mossadams.com	Rachel.Laureno@mossadams.com	Rachel	Laureno	819	Professional Affiliate
tony.andrade@mossadams.com	tony.andrade@mossadams.com	Tony	Andrade	819	Professional Affiliate
William.norris@mossadams.com	William.norris@mossadams.com	William	Norris	819	Professional Affiliate
Josh.Lewis@mossadams.com	Josh.Lewis@mossadams.com	Josh	Lewis	819	Professional Affiliate
ken@healthcrowd.com	ken@healthcrowd.com	Ken	Mobley	819	Affiliate
leslie@healthcrowd.com	leslie@healthcrowd.com	Leslie	Groves	819	Affiliate
annemieke@healthcrowd.com	annemieke@healthcrowd.com	Annemieke	Umberg	819	Affiliate
bing@healthcrowd.com	bing@healthcrowd.com	Bing	Doh	819	Affiliate
jackie@healthcrowd.com	jackie@healthcrowd.com	Jackie	Maynard	819	Affiliate
christian@healthcrowd.com	christian@healthcrowd.com	Christian	Bagge	819	Affiliate
josette@healthcrowd.com	josette@healthcrowd.com	Josette	Lee	819	Affiliate
nora.cristobal@mpulsemobile.com	nora.cristobal@mpulsemobile.com	Nora	Cristobal	819	Affiliate
alaina.tackett@mpulsemobile.com	alaina.tackett@mpulsemobile.com	Alaina	Tackett	819	Affiliate
pstalboerger@mtm-inc.net	pstalboerger@mtm-inc.net	Phil	Stalboerger	819	Associate
jhericks@mtm-inc.net	jhericks@mtm-inc.net	Jill	Hericks	819	Associate
kprice@mtm-inc.net	kprice@mtm-inc.net	Katie	Price	819	Associate
mlucas@mtm-inc.net	mlucas@mtm-inc.net	Michele	Lucas	819	Associate
joelsmith@mtm-inc.net	joelsmith@mtm-inc.net	Joel	Smith	819	Associate
ahazzard@e-nva.com	ahazzard@e-nva.com	Andrea	Hazzard	819	Associate
rrenna@e-nva.com	rrenna@e-nva.com	Rick	Renna	819	Associate
mgilmore@e-nva.com	mgilmore@e-nva.com	Michelle	Gilmore	819	Associate
cmoroff@e-nva.com	cmoroff@e-nva.com	Carl	Moroff	819	Associate
michelle.kroll@benecard.com	michelle.kroll@benecard.com	Michelle	Kroll	819	Associate
ahazzard@e-nva.com	ahazzard@e-nva.com	Andrea	Hazzard	819	Associate
mgilmore@e-nva.com	mgilmore@e-nva.com	Michelle	Gilmore	819	Associate
david.fields@navitus.com	david.fields@navitus.com	David	Fields	820	PBM Member Employee
sarah.schnell@navitus.com	sarah.schnell@navitus.com	Sarah	Schnell	820	PBM Member Employee
gayle.fisher@navitus.com	gayle.fisher@navitus.com	Gayle	Fisher	820	PBM Member Employee
collan.rosier@navitus.com	collan.rosier@navitus.com	Collan	Rosier	820	PBM Member Employee
byron.mickle@navitus.com	byron.mickle@navitus.com	Byron	Mickle	820	PBM Member Employee
rachel.breger@navitus.com	rachel.breger@navitus.com	Rachel	Breger	820	PBM Member Employee
michael.bevins@navitus.com	michael.bevins@navitus.com	Michael	Bevins	820	PBM Member Employee
donna.bentley@navitus.com	donna.bentley@navitus.com	Donna	Bentley	820	PBM Member Employee
tom.pabich@navitus.com	tom.pabich@navitus.com	Tom	Pabich	820	PBM Member Employee
tonnlarry@gmail.com	tonnlarry@gmail.com	Larry	Tonn	820	PBM Member Employee
robyn.crosson@navitus.com	robyn.crosson@navitus.com	Robyn	Crosson	820	PBM Member Employee
Kimberly.Rogers@navitus.com	Kimberly.Rogers@navitus.com	Kimberly	Rogers	820	PBM Member Employee
penny.avery@novartis.com	penny.avery@novartis.com	Penny	Avery	819	Affiliate
jody.amodeo@novartis.com	jody.amodeo@novartis.com	Jody	Amodeo	819	Affiliate
robert.zahid@novartis.com	robert.zahid@novartis.com	Robert	Zahid	819	Affiliate
peter.trask@changehealthcare.com	peter.trask@changehealthcare.com	Peter	Trask	819	Affiliate
denise.louden@optum.com	denise.louden@optum.com	Denise	Louden	819	Affiliate
wally.danielson@optum.com	wally.danielson@optum.com	Wally	Danielson	819	Affiliate
fonsecah@advisory.com	fonsecah@advisory.com	Hepzi	Fonseca	819	Affiliate
allison.pogue@optum.com	allison.pogue@optum.com	Allison	Pogue	819	Affiliate
yokleyb@advisory.com	yokleyb@advisory.com	Brian	Yokley	819	Affiliate
bglaeser@changehealthcare.com	bglaeser@changehealthcare.com	Buffi	Glaeser	819	Affiliate
michael.creech@mckesson.com	michael.creech@mckesson.com	Michael	Creech	819	Affiliate
ahall@changehealthcare.com	ahall@changehealthcare.com	Annalis	Hall	819	Affiliate
peter.firehammer@changehealthcare.com	peter.firehammer@changehealthcare.com	Peter	Firehammer	819	Affiliate
david.kaskoun@gmail.com	david.kaskoun@gmail.com	David	kaskoun	819	Affiliate
chuck.wacker@optum.com	chuck.wacker@optum.com	Chuck	Wacker	819	Affiliate
bhoover@changehealthcare.com	bhoover@changehealthcare.com	Bill	Hoover	819	Affiliate
trebesn@advisory.com	trebesn@advisory.com	Natalie	Trebes	819	Affiliate
martha.herbig@optum.com	martha.herbig@optum.com	Martha	Herbig	819	Affiliate
phillip.king@changehealthcare.com	phillip.king@changehealthcare.com	Phillip	King	819	Affiliate
dgallegos@changehealthcare.com	dgallegos@changehealthcare.com	David	Gallegos	819	Affiliate
kimsal@advisory.com	kimsal@advisory.com	Sally	Kim	819	Affiliate
susan.sivertsen@optum.com	susan.sivertsen@optum.com	Susan	Sivertsen	819	Affiliate
loren.koerber@optum.com	loren.koerber@optum.com	Loren	Koerber	819	Affiliate
Jessica.Marshall1@changehealthcare.com	Jessica.Marshall1@changehealthcare.com	Jessica	Marshall	819	Affiliate
Candy.Chambers@changehealthcare.com	Candy.Chambers@changehealthcare.com	Candy	Chambers	819	Affiliate
WGeis@changehealthcare.com	WGeis@changehealthcare.com	Wani	Geis	819	Affiliate
Danna.Ruppel@changehealthcare.com	Danna.Ruppel@changehealthcare.com	Danna	Ruppel	819	Affiliate
bewell@hioscar.com	bewell@hioscar.com	Benjamin	Ewell	823	Health Plan Employee
jslayton@hioscar.com	jslayton@hioscar.com	Jess	Slayton	823	Health Plan Employee
meera@hioscar.com	meera@hioscar.com	Meera	Atkins	823	Health Plan Employee
wjohnson@hioscar.com	wjohnson@hioscar.com	Will	Johnson	823	Health Plan Employee
smartin@hioscar.com	smartin@hioscar.com	Sean	Martin	823	Health Plan Employee
mpearce@hioscar.com	mpearce@hioscar.com	Matthew	Pearce	823	Health Plan Employee
kbaumann@hioscar.com	kbaumann@hioscar.com	Kristy	Baumann	823	Health Plan Employee
csebastian@hioscar.com	csebastian@hioscar.com	Carmella	Sebastian	823	Health Plan Employee
tward@hioscar.com	tward@hioscar.com	Tamara	Ward	823	Health Plan Employee
missi@hioscar.com	missi@hioscar.com	Missi	Zook	823	Health Plan Employee
jvecchiet@hioscar.com	jvecchiet@hioscar.com	Jonathan	Vecchiet	823	Health Plan Employee
rich@hioscar.com	rich@hioscar.com	Rich	Loconte	823	Health Plan Employee
apapsun@hioscar.com	apapsun@hioscar.com	Amy	Papsun	823	Health Plan Employee
jones@hioscar.com	jones@hioscar.com	Kevin	Jones	823	Health Plan Employee
cgrason@hioscar.com	cgrason@hioscar.com	Cathy	Grason	823	Health Plan Employee
alanna@hioscar.com	alanna@hioscar.com	Alanna	Powers	823	Health Plan Employee
mya@hioscar.com	mya@hioscar.com	Mya	Strauss	823	Health Plan Employee
mario@hioscar.com	mario@hioscar.com	Mario	Schlosser	823	Health Plan Employee
krice@hioscar.com	krice@hioscar.com	Kaitlyn	Rice	823	Health Plan Employee
raxelrod@hioscar.com	raxelrod@hioscar.com	Robert	Axelrod	823	Health Plan Employee
mpasnik@hioscar.com	mpasnik@hioscar.com	Michael	Pasnik	823	Health Plan Employee
sorrange@hioscar.com	sorrange@hioscar.com	Sara	Orrange	823	Health Plan Employee
jtredway@hioscar.com	jtredway@hioscar.com	Jeffrey "Ryan"	Tredway	823	Health Plan Employee
ava.norris@phhs.org	ava.norris@phhs.org	Ava	Norris	823	Health Plan Employee
khurram.taufiq@phhs.org	khurram.taufiq@phhs.org	Khurram	Taufiq	823	Health Plan Employee
david.bartoszek@phhs.org	david.bartoszek@phhs.org	Matt	Bartoszek	823	Health Plan Employee
amrita.waingankar@phhs.org	amrita.waingankar@phhs.org	Amrita	Waingankar	823	Health Plan Employee
tamara.willie@phhs.org	tamara.willie@phhs.org	Tamara	Willie	823	Health Plan Employee
margaret.roche@phhs.org	margaret.roche@phhs.org	Margaret	Roche, PhD	823	Health Plan Employee
peter.waziri@phhs.org	peter.waziri@phhs.org	Peter	Waziri	823	Health Plan Employee
nicholas.smith@phhs.org	nicholas.smith@phhs.org	Nicholas	Smith	823	Health Plan Employee
nakia.smith@phhs.org	nakia.smith@phhs.org	Nakia	Smith	823	Health Plan Employee
andrew.shapiro@phhs.org	andrew.shapiro@phhs.org	Andrew	Shapiro	823	Health Plan Employee
tamara.gavin@phhs.org	tamara.gavin@phhs.org	Tamera	Gavin	823	Health Plan Employee
kellie.philpot@phhs.org	kellie.philpot@phhs.org	Kellie	Philpot	823	Health Plan Employee
justin.skerbetz@phhs.org	justin.skerbetz@phhs.org	justin	skerbetz	823	Health Plan Employee
paula.turicchi@phhs.org	paula.turicchi@phhs.org	Paula	Turicchi	823	Health Plan Employee
jeniffer.gonzalez@phhs.org	jeniffer.gonzalez@phhs.org	Jennifer	Gonzalez	823	Health Plan Employee
melissa.zook@phhs.org	melissa.zook@phhs.org	Missi	Zook	823	Health Plan Employee
michael.deluna@phhs.org	michael.deluna@phhs.org	Michael	de Luna	823	Health Plan Employee
jane.stegall@phhs.org	jane.stegall@phhs.org	Meredith	Stegall	823	Health Plan Employee
susan.libson@phhs.org	susan.libson@phhs.org	Susan	Libson	823	Health Plan Employee
lee.deluna@phhs.org	lee.deluna@phhs.org	Lee	DeLuna	823	Health Plan Employee
felicia.ramirez@phhs.org	felicia.ramirez@phhs.org	Felicia	Ramirez	823	Health Plan Employee
cheryl.edwards@phhs.org	cheryl.edwards@phhs.org	Cheryl	Edwards	823	Health Plan Employee
karshena.valsin@phhs.org	karshena.valsin@phhs.org	Karshena	Valsin	823	Health Plan Employee
Reigen.lox@phhs.org	Reigen.lox@phhs.org	Reigen	Lox	823	Health Plan Employee
paula.turicchi@gmail.com	paula.turicchi@gmail.com	Paula	Turicchi	823	Health Plan Employee
Jill.terrymichener@phhs.org	Jill.terrymichener@phhs.org	Jill	Terry Michener	823	Health Plan Employee
suzanne.faulkenberry@phhs.org	suzanne.faulkenberry@phhs.org	Suzanne	Faulkenberry	823	Health Plan Employee
amanda.hudgens@phhs.org	amanda.hudgens@phhs.org	Amanda	Hudgens	823	Health Plan Employee
NEEL.PATEL@phhs.org	NEEL.PATEL@phhs.org
reigen.lox@phhs.org	reigen.lox@phhs.org	Reigen	Lox	823	Health Plan Employee
Victoria.Mora@phhs.org	Victoria.Mora@phhs.org	Victoria	Mora	823	Health Plan Employee
Amanda.hudgens@phhs.org	Amanda.hudgens@phhs.org	Amanda	Hudgens	823	Health Plan Employee
graham.keever@phhs.org	graham.keever@phhs.org	Graham	Keever	823	Health Plan Employee
katherine.yoder@phhs.org	katherine.yoder@phhs.org	Katherine	Yoder	823	Health Plan Employee
tom.murar@phhs.org	tom.murar@phhs.org	Tom	Murar	823	Health Plan Employee
gordon.davis@phhs.org	gordon.davis@phhs.org	Gordon	Davis	823	Health Plan Employee
mshrader@pcmanet.org	mshrader@pcmanet.org	Melodie	Shrader	820	PBM Member Employee
pfjelstad@pcmanet.org	pfjelstad@pcmanet.org	Peter	Fjelstad	820	PBM Member Employee
me@mindyellmer.com	me@mindyellmer.com	Mindy	Ellmer	820	PBM Member Employee
kim@podimetrics.com	kim@podimetrics.com	Kim	Carpenter		Affiliate
simon@podimetrics.com	simon@podimetrics.com	Simon	Salgado		Affiliate
nicole@podimetrics.com	nicole@podimetrics.com	Nicole	Neff		Affiliate
jon@podimetrics.com	jon@podimetrics.com	Jon	Bloom		Affiliate
davidica@podimetrics.com	davidica@podimetrics.com	Davidica	Brodersen		Affiliate
droot@primetherapeutics.com	droot@primetherapeutics.com	David	Root	820	PBM Member Employee
ptwohy@primetherapeutics.com	ptwohy@primetherapeutics.com	Patrick	Twohy	820	PBM Member Employee
lmendezharper@primetherapeutics.com	lmendezharper@primetherapeutics.com	LuGina	Mendez-Harper, PharmD	820	PBM Member Employee
caitlin.berry@primetherapeutics.com	caitlin.berry@primetherapeutics.com	Catilin	Berry	820	PBM Member Employee
jamo.rubin@rightsitehealth.com	jamo.rubin@rightsitehealth.com				Affiliate
jamo.rubin@rightsitehealth.com	jamo.rubin@rightsitehealth.com	Jamo	Rubin, MD		Affiliate
robbins@saferidehealth.com	robbins@saferidehealth.com	Robbins	Schrader		Associate
josh@saferidehealth.com	josh@saferidehealth.com	Joshua	Blumenfeld		Associate
patrick@saferidehealth.com	patrick@saferidehealth.com	Patrick	Egan		Associate
andy@saferidehealth.com	andy@saferidehealth.com	Andy	Auerbach		Associate
carolyn@saferidehealth.com	carolyn@saferidehealth.com	Carolyn	Bergin		Associate
david@saferidehealth.com	david@saferidehealth.com	David	Constantine		Associate
ben@saferidehealth.com	ben@saferidehealth.com	Ben	Salter		Associate
ashley@saferidehealth.com	ashley@saferidehealth.com	Ashely	Roberst		Associate
dpipkin@sarepta.com	dpipkin@sarepta.com	Dana	Pipkin		Affiliate
ccaldwell@sarepta.com	ccaldwell@sarepta.com	Casey	Caldwell		Affiliate
swhite@scanhealthplan.com	swhite@scanhealthplan.com	Sharrah	White		Health Plan Employee
GHawkins@scanhealthplan.com	GHawkins@scanhealthplan.com	Ginette	Hawkins		Health Plan Employee
DHoward@scanhealthplan.com	DHoward@scanhealthplan.com	Donna	Howard		Health Plan Employee
WZhao@scanhealthplan.com	WZhao@scanhealthplan.com	Wendy	Zhao		Health Plan Employee
s.ramalingam@bswhealth.org	s.ramalingam@bswhealth.org	S	Ramalingam		Health Plan Employee
cathy.caswell@bswhealth.org	cathy.caswell@bswhealth.org	Cathy	Caswell		Health Plan Employee
amber.burgos@bswhealth.org	amber.burgos@bswhealth.org	Amber	Burgos		Health Plan Employee
maureen.martin@bswhealth.org	maureen.martin@bswhealth.org	Maureen	Martin		Health Plan Employee
sharon.saravia@bswhealth.org	sharon.saravia@bswhealth.org	Sharon	Saravia		Health Plan Employee
felicia.smith@bswhealth.org	felicia.smith@bswhealth.org	Felicia	Smith		Health Plan Employee
karen.baratta@bswhealth.org	karen.baratta@bswhealth.org	Karen	Baratta		Health Plan Employee
david.ellis@bswhealth.org	david.ellis@bswhealth.org	David	Ellis		Health Plan Employee
basma.khurshid@bswhealth.org	basma.khurshid@bswhealth.org	Basma	Khurshid		Health Plan Employee
susan.balezentis@bswhealth.org	susan.balezentis@bswhealth.org	Susan	Balezentis		Health Plan Employee
amy.cornett@bswhealth.org	amy.cornett@bswhealth.org	Amy	Cornett		Health Plan Employee
vilaida.rivera@bswhealth.org	vilaida.rivera@bswhealth.org	Vilaida	Rivera		Health Plan Employee
dipali.portwood@bswhealth.org	dipali.portwood@bswhealth.org	Dipali	Portwood		Health Plan Employee
lisa.fillip@bswhealth.org	lisa.fillip@bswhealth.org	Lisa	Fillip		Health Plan Employee
mary.field@bswhealth.org	mary.field@bswhealth.org	Mary	Field		Health Plan Employee
natalie.rivera@bswhealth.org	natalie.rivera@bswhealth.org	Natalie	Rivera		Health Plan Employee
danielle.jaber@bswhealth.org	danielle.jaber@bswhealth.org	Danielle	Jaber		Health Plan Employee
erica.martin@bswhealth.org	erica.martin@bswhealth.org	Erica	Martin		Health Plan Employee
lauren.russell1@bswhealth.org	lauren.russell1@bswhealth.org	Lauren	Russell		Health Plan Employee
chastidy.artis@bswhealth.org	chastidy.artis@bswhealth.org	Chastidy	Artis		Health Plan Employee
marisa.finley@bswhealth.org	marisa.finley@bswhealth.org	Marisa	Finley		Health Plan Employee
evelyn.gabrillo@bswhealth.org	evelyn.gabrillo@bswhealth.org	Evelyn	Gabrillo		Health Plan Employee
lindsay.manning@bswhealth.org	lindsay.manning@bswhealth.org	Lindsay	Manning		Health Plan Employee
theresa.magellan@bswhealth.org	theresa.magellan@bswhealth.org	Theresa	Magellan		Health Plan Employee
megan.cunningham@bswhealth.org	megan.cunningham@bswhealth.org	Megan	Cunningham		Health Plan Employee
jessica.sullivan1@bswhealth.org	jessica.sullivan1@bswhealth.org	Jessica	Sullivan		Health Plan Employee
timothy.tasset@bswhealth.org	timothy.tasset@bswhealth.org	Timothy	Tasset		Health Plan Employee
elizabeth.lopezcepero@bswhealth.org	elizabeth.lopezcepero@bswhealth.org	Liz	Lopez Cepero		Health Plan Employee
kristi.sherrill@bswhealth.org	kristi.sherrill@bswhealth.org	Kristi	Sherrill		Health Plan Employee
stacey.byrd@bswhealth.org	stacey.byrd@bswhealth.org	Stacey	Byrd		Health Plan Employee
ellen.verzino@bswhealth.org	ellen.verzino@bswhealth.org	Ellen	Verzino		Health Plan Employee
leonardo.gutierrez@bswhealth.org	leonardo.gutierrez@bswhealth.org	Leonardo	Gutierrez		Health Plan Employee
jason.tipton@bswhealth.org	jason.tipton@bswhealth.org	Jason	Tipton		Health Plan Employee
mico.adams@bswhealth.org	mico.adams@bswhealth.org	Nico	Adams		Health Plan Employee
kathleen.martin@bswhealth.org	kathleen.martin@bswhealth.org	Katie	Martin		Health Plan Employee
ira.bell@bswhealth.org	ira.bell@bswhealth.org	Ira	Bell		Health Plan Employee
david.krauss@bswhealth.org	david.krauss@bswhealth.org	David	Krauss		Health Plan Employee
Chmyra.Starks@BSWHealth.org	Chmyra.Starks@BSWHealth.org	Chmyra	Starks		Health Plan Employee
Jenny.Garcia1@bswhealth.org	Jenny.Garcia1@bswhealth.org	Jenny	Garcia		Health Plan Employee
charlotte.luebbert@BSWhealth.org	charlotte.luebbert@BSWhealth.org	Charlotte	Luebbert		Health Plan Employee
daniel.posey@bswhealth.org	daniel.posey@bswhealth.org	Daniel	Posey		Health Plan Employee
lydia.best@bswhealth.org	lydia.best@bswhealth.org	Lydia	Best		Health Plan Employee
SUBROWN@sw.org	SUBROWN@sw.org	Susan	Brown		Health Plan Employee
wendy.brownlee@bswhealth.org	wendy.brownlee@bswhealth.org	Wendy	Brownlee		Health Plan Employee
Amanda.Pittman@bswhealth.org	Amanda.Pittman@bswhealth.org	Amanda	Pittman		Health Plan Employee
Jennifer.Boreing@bswhealth.org	Jennifer.Boreing@bswhealth.org	Jennifer	Boreing		Health Plan Employee
Kristy.Bulhoes@bswhealth.org	Kristy.Bulhoes@bswhealth.org	Kristy	Bulhoes		Health Plan Employee
Tara.Stafford@bswhealth.org	Tara.Stafford@bswhealth.org	Tara	Stafford		Health Plan Employee
Richard.Reuter@bswhealth.org	Richard.Reuter@bswhealth.org	Richard	Reuter		Health Plan Employee
John.Majors@bswhealth.org	John.Majors@bswhealth.org	John	Majors		Health Plan Employee
sirika.clayton@bswhealth.org	sirika.clayton@bswhealth.org	Sirika	Clayton		Health Plan Employee
Neil.Bhakta@bswhealth.org	Neil.Bhakta@bswhealth.org	Neil	Bhakta		Health Plan Employee
heather.ueckert@bswhealth.org	heather.ueckert@bswhealth.org	Heather	Ueckhert		Health Plan Employee
opal.galliano@bswhealth.org	opal.galliano@bswhealth.org	Opal	Galliano		Health Plan Employee
elizabeth.lopezcepero@bswhealth.org	elizabeth.lopezcepero@bswhealth.org	Lopez	Elizabeth		Health Plan Employee
Kimberley.Adda@bswhealth.org	Kimberley.Adda@bswhealth.org	Kimberley	Adda		Health Plan Employee
Anita.Hart@bswhealth.org	Anita.Hart@bswhealth.org	Anita	Hart		Health Plan Employee
anita.hart@bswhealth.org	anita.hart@bswhealth.org	Anita	Hart		Health Plan Employee
Stacie.walkerposvar@bswhealth.org	Stacie.walkerposvar@bswhealth.org	Stacie	Walker-Posvar		Health Plan Employee
Amanda.Trapasso@BSWHealth.org	Amanda.Trapasso@BSWHealth.org	Amanda	Trapasso		Health Plan Employee
laci.noble@bswhealth.org	laci.noble@bswhealth.org	Laci	Noble		Health Plan Employee
Nichole.Whited@bswhealth.org	Nichole.Whited@bswhealth.org	Nichole	Hill		Health Plan Employee
Cristal.Detert@bswhealth.org	Cristal.Detert@bswhealth.org
Roger.HarrisPates@bswhealth.org	Roger.HarrisPates@bswhealth.org
Andrew.Berg@bswhealth.org	Andrew.Berg@bswhealth.org
Patsy.Vrazel@bswhealth.org	Patsy.Vrazel@bswhealth.org
Tracie.Acosta@bswhealth.org	Tracie.Acosta@bswhealth.org
Esther.Webb@bswhealth.org	Esther.Webb@bswhealth.org
melissa.rosson@bswhealth.org	melissa.rosson@bswhealth.org	Melissa	Rosson		Health Plan Employee
jeffrey.ingrum@bswhealth.org	jeffrey.ingrum@bswhealth.org	Jeffrey	Ingrum		Health Plan Employee
deborah.cotton@bswhealth.org	deborah.cotton@bswhealth.org	Deborah	Cotton		Health Plan Employee
tamara.caldwell@bswhealth.org	tamara.caldwell@bswhealth.org	Tamara	Caldwell		Health Plan Employee
jessica.olson2@bswhealth.org	jessica.olson2@bswhealth.org	Jessica	Olson		Health Plan Employee
suzanne.brown@bswhealth.org	suzanne.brown@bswhealth.org	Suzanne	Brown		Health Plan Employee
jesse.sifuentez@bswhealth.org	jesse.sifuentez@bswhealth.org	Jesse	Sifuentez		Health Plan Employee
gjessee@sellersdorsey.com	gjessee@sellersdorsey.com	Gary	Jessee		Affiliate
tko@sellersdorsey.com	tko@sellersdorsey.com	Tiffany	Ko		Affiliate
jfagen@sellersdorsey.com	jfagen@sellersdorsey.com	Janice	Fagen		Affiliate
sludher@sellersdorsey.com	sludher@sellersdorsey.com	Sharen	Ludher		Affiliate
pamela.piatt@senderohealth.com	pamela.piatt@senderohealth.com	Pamela	Piatt		Health Plan Employee
rosemary.ang@senderohealth.com	rosemary.ang@senderohealth.com	Rosemary	Ang		Health Plan Employee
ashlea.tolbert@senderohealth.com	ashlea.tolbert@senderohealth.com	Ashlea	Tolbert		Health Plan Employee
misty.smith@senderohealth.com	misty.smith@senderohealth.com	Misty	Smith		Health Plan Employee
perla.cavazos@centralhealth.net	perla.cavazos@centralhealth.net	Perla	Cavazos		Health Plan Employee
theresa.bedinghaus@senderohealth.com	theresa.bedinghaus@senderohealth.com	Theresa	Bedinghaus		Health Plan Employee
alfonso.rubio@senderohealth.com	alfonso.rubio@senderohealth.com	Alfonso	Rubio		Health Plan Employee
stephanie.mendez@senderohealth.com	stephanie.mendez@senderohealth.com	Stephanie	Mendez		Health Plan Employee
stacy.leon@senderohealth.com	stacy.leon@senderohealth.com	Stacy	Leon		Health Plan Employee
yaremi.cortez@senderohealth.com	yaremi.cortez@senderohealth.com	Yaremi	Cortez		Health Plan Employee
compliance@senderohealth.com	compliance@senderohealth.com	Sendero	Compliance		Health Plan Employee
marycarol.jennings@senderohealth.com	marycarol.jennings@senderohealth.com	Mary Carol	Jennings		Health Plan Employee
amber.allbritten@senderohealth.com	amber.allbritten@senderohealth.com	Amber	Allbritten		Health Plan Employee
ted.held@senderohealth.com	ted.held@senderohealth.com	Ted	Held		Health Plan Employee
rodolfor.ybarra@senderohealth.com	rodolfor.ybarra@senderohealth.com	Rudy	Ybarra		Health Plan Employee
elizabeth.barreneche@senderohealth.com	elizabeth.barreneche@senderohealth.com	Elizabeth	Barreneche		Health Plan Employee
tierra.thomas@senderohealth.com	tierra.thomas@senderohealth.com	Tierra	Thomas		Health Plan Employee
celso.baez@centralhealth.net	celso.baez@centralhealth.net	Ceslo	Baez		Health Plan Employee
pastora.galvez@senderohealth.com	pastora.galvez@senderohealth.com	Pastora	Galvez		Health Plan Employee
matthew.keats@senderohealth.com	matthew.keats@senderohealth.com	Matthew	Keats		Health Plan Employee
Yvette.Bates-Coleman@senderohealth.com	Yvette.Bates-Coleman@senderohealth.com	Yvette	Bates-Coleman		Health Plan Employee
Paul.Emerson@centralhealth.net	Paul.Emerson@centralhealth.net	Paul	Emerson		Health Plan Employee
Perla.Cavazos@senderohealth.com	Perla.Cavazos@senderohealth.com	Perla	Cavazos		Health Plan Employee
charles.gilham@ascension.org	charles.gilham@ascension.org	Charlie	Gilham		Health Plan Employee
adean2@ascension.org	adean2@ascension.org	Amanda	Dean		Health Plan Employee
saszucs@ascension.org	saszucs@ascension.org	Shelley	Szucs		Health Plan Employee
tkillebrew@ascension.org	tkillebrew@ascension.org	Tammy	Killebrew		Health Plan Employee
akennedy@ascension.org	akennedy@ascension.org	Anne	Kennedy		Health Plan Employee
janet.walker@ascension.org	janet.walker@ascension.org	Janet	Walker		Health Plan Employee
emiliano.romero@ascension.org	emiliano.romero@ascension.org	Emiliano	Romero		Health Plan Employee
kaedwards@ascension.org	kaedwards@ascension.org	Kimberly	Edwards MD		Health Plan Employee
aromero@ascension.org	aromero@ascension.org	Alexandria	Romero		Health Plan Employee
grodriguez1@ascension.org	grodriguez1@ascension.org	Geronimo	Rodriguez		Health Plan Employee
suffelman@ascension.org	suffelman@ascension.org	Stacey	Uffelman		Health Plan Employee
sharon.jandrain@ascension.org	sharon.jandrain@ascension.org	Sharon	Jandrain		Health Plan Employee
Sara.Daugherty@ascension.org	Sara.Daugherty@ascension.org	Sara	Daugherty		Health Plan Employee
kristine.norris@ascension.org	kristine.norris@ascension.org	Kristine	Norris		Health Plan Employee
susan.balezentis@ascension.org	susan.balezentis@ascension.org	Susan	Balezentis		Health Plan Employee
adolfo.valadez@ascension.org	adolfo.valadez@ascension.org	adolfo	Valadez		Health Plan Employee
mvnguyen2@ascension.org	mvnguyen2@ascension.org	Michael	Nguyen		Health Plan Employee
sara.daugherty@ascension.org	sara.daugherty@ascension.org	Sarah	Daugherty		Health Plan Employee
cynthia.davis1@ascension.org	cynthia.davis1@ascension.org	Cynthia	Davis		Health Plan Employee
nicole.nealey@ascension.org	nicole.nealey@ascension.org	Nicole	Nealey		Health Plan Employee
marinan.williams@ascension.org	marinan.williams@ascension.org	Marinan	Williams		Health Plan Employee
rosievmcstay@rvmstrategies.net	rosievmcstay@rvmstrategies.net	Rosie	McStay		Health Plan Employee
paul.tannos@ascension.org	paul.tannos@ascension.org	Paul	Tannos		Health Plan Employee
marc.parker@sunovion.com	marc.parker@sunovion.com	Marc	Parker		Affiliate
scott.hylla@sunovion.com	scott.hylla@sunovion.com	Scott	Hylla		Affiliate
mario.freeman@sunovion.com	mario.freeman@sunovion.com	Mario	Freeman		Affiliate
jeffrey.simon@superiorhealthplan.com	jeffrey.simon@superiorhealthplan.com	Jeffrey	Simon		Health Plan Employee
cleo.diom@superiorhealthplan.com	cleo.diom@superiorhealthplan.com	Cleo	Diom		Health Plan Employee
albert@hawkinsppc.com	albert@hawkinsppc.com	Albert	Hawkins		Health Plan Contract Lobbyist
rachelle.palima@superiorhealthplan.com	rachelle.palima@superiorhealthplan.com	Rachelle	Palima		Health Plan Employee
shan.song@centene.com	shan.song@centene.com	Shan	Song		Health Plan Employee
esmeralda.cazares-baig@superiorhealthplan.com	esmeralda.cazares-baig@superiorhealthplan.com	Esmerelda	Cazares-Baig		Health Plan Employee
allison.swartz@superiorhealthplan.com	allison.swartz@superiorhealthplan.com	Allison	Swartz		Health Plan Employee
patricia.correa@superiorhealthplan.com	patricia.correa@superiorhealthplan.com	Patricia	Correa		Health Plan Employee
tracy.rico@superiorhealthplan.com	tracy.rico@superiorhealthplan.com	Tracy	Rico		Health Plan Employee
calvin.williams@superiorhealthplan.com	calvin.williams@superiorhealthplan.com	Calvin	Williams		Health Plan Employee
jocelyn.zimmerle@superiorhealthplan.com	jocelyn.zimmerle@superiorhealthplan.com	Jocelyn	Zimmerle		Health Plan Employee
narcedalia.aguayo@superiorhealthplan.com	narcedalia.aguayo@superiorhealthplan.com	Narcedalia	Aquayo		Health Plan Employee
angel.duran@superiorhealthplan.com	angel.duran@superiorhealthplan.com	Angel	Duran		Health Plan Employee
john.waidner@superiorhealthplan.com	john.waidner@superiorhealthplan.com	John	Waidner		Health Plan Employee
alex.goldson@superiorhealthplan.com	alex.goldson@superiorhealthplan.com	Alex	Goldson		Health Plan Employee
amanda.r.shaw@centene.com	amanda.r.shaw@centene.com	Amanda	Shaw		Health Plan Employee
mraleigh@centene.com	mraleigh@centene.com	Michelle	Raleigh		Health Plan Employee
brendle.glomb@superiorhealthplan.com	brendle.glomb@superiorhealthplan.com	Brendle	Glomb		Health Plan Employee
lacy.slaughter@superiorhealthplan.com	lacy.slaughter@superiorhealthplan.com	Lacy	Slaughter		Health Plan Employee
malinda.buratti@superiorhealthplan.com	malinda.buratti@superiorhealthplan.com	Malinda	Buratti		Health Plan Employee
ben.hamm@superiorhealthplan.com	ben.hamm@superiorhealthplan.com	Ben	Hamm		Health Plan Employee
robert.barone@superiorhealthplan.com	robert.barone@superiorhealthplan.com	Robert	Barone		Health Plan Employee
jenmiller@centene.com	jenmiller@centene.com	Jenifer	Miller		Health Plan Employee
michelle.murdock@superiorhealthplan.com	michelle.murdock@superiorhealthplan.com	Michelle	Murdock		Health Plan Employee
rene.pena2@superiorhealthplan.com	rene.pena2@superiorhealthplan.com	Rene	Pena		Health Plan Employee
teresa.kahan@superiorhealthplan.com	teresa.kahan@superiorhealthplan.com	Teresa	Kahan		Health Plan Employee
julie.smith@superiorhealthplan.com	julie.smith@superiorhealthplan.com	Julie	Smith		Health Plan Employee
karen.westbay@superiorhealthplan.com	karen.westbay@superiorhealthplan.com	Karen	Westbay		Health Plan Employee
reed@crestline-solutions.com	reed@crestline-solutions.com	Reed	Clay		Health Plan Contract Lobbyist
dkillian@centene.com	dkillian@centene.com	Don	Killian		Health Plan Employee
cari.cates@superiorhealthplan.com	cari.cates@superiorhealthplan.com	Cari	Cates		Health Plan Employee
james.m.robson@centene.com	james.m.robson@centene.com	James	Robson		Health Plan Employee
regulatory.compliance@superiorhealthplan.com	regulatory.compliance@superiorhealthplan.com	Regulatory	Compliance		Health Plan Employee
tanya.wells@superiorhealthplan.com	tanya.wells@superiorhealthplan.com	Tanya	Wells		Health Plan Employee
perla.arce-franke@superiorhealthplan.com	perla.arce-franke@superiorhealthplan.com	Perla	Arce-Franke		Health Plan Employee
jennifer.gasior@superiorhealthplan.com	jennifer.gasior@superiorhealthplan.com	Jennifer	Gasior		Health Plan Employee
marissa.livingston@superiorhealthplan.com	marissa.livingston@superiorhealthplan.com	Marissa	Livingston		Health Plan Employee
vanessa.sportsman@superiorhealthplan.com	vanessa.sportsman@superiorhealthplan.com	Vanessa	Sportsman		Health Plan Employee
albert.lopez@superiorhealthplan.com	albert.lopez@superiorhealthplan.com	Albert	Lopez		Health Plan Employee
jennifer.shipman@superiorhealthplan.com	jennifer.shipman@superiorhealthplan.com	Jennifer	Shipman		Health Plan Employee
sara.robins@superiorhealthplan.com	sara.robins@superiorhealthplan.com	Sara	Robins		Health Plan Employee
michelle.mitchell@superiorhealthplan.com	michelle.mitchell@superiorhealthplan.com	Michelle	Mitchell		Health Plan Employee
susan.deville@superiorhealthplan.com	susan.deville@superiorhealthplan.com	Susan	DeVille		Health Plan Employee
debra.danziger@superiorhealthplan.com	debra.danziger@superiorhealthplan.com	Debra	Danziger		Health Plan Employee
rowells@centene.com	rowells@centene.com	Robert	Wells		Health Plan Employee
ambar.qureshi@superiorhealthplan.com	ambar.qureshi@superiorhealthplan.com	Ambar	Qureshi		Health Plan Employee
cecilia.barraza@superiorhealthplan.com	cecilia.barraza@superiorhealthplan.com	Cecilia	Barraza		Health Plan Employee
patrick.kovalik@superiorhealthplan.com	patrick.kovalik@superiorhealthplan.com	Patrick	Kovalik		Health Plan Employee
destine.rawls@superiorhealthplan.com	destine.rawls@superiorhealthplan.com	Destine	Rawls		Health Plan Employee
kfreeman@centene.com	kfreeman@centene.com	Katelind	Freeman		Health Plan Employee
anna.velasquez@superiorhealthplan.com	anna.velasquez@superiorhealthplan.com	Anna	Velaquez		Health Plan Employee
lenore.depagter@superiorhealthplan.com	lenore.depagter@superiorhealthplan.com	Lenore	DePagter		Health Plan Contract Lobbyist
cheryl.cizler@superiorhealthplan.com	cheryl.cizler@superiorhealthplan.com	Cheryl	Cizler		Health Plan Employee
denise.herrera@superiorhealthplan.com	denise.herrera@superiorhealthplan.com	Denise	Herrera		Health Plan Employee
shereen.jensen@wellcare.com	shereen.jensen@wellcare.com	Shereen	Jensen		Health Plan Employee
jenn@phenixsaenz.com	jenn@phenixsaenz.com	Jenn	Saenz		Health Plan Contract Lobbyist
sandra.vale@superiorhealthplan.com	sandra.vale@superiorhealthplan.com	Sandy	Vale		Health Plan Employee
cathy@schluetergroup.com	cathy@schluetergroup.com	Cathy	DeWitt		Health Plan Contract Lobbyist
tom.shock@superiorhealthplan.com	tom.shock@superiorhealthplan.com	Tom	Shock		Health Plan Employee
sara.pena@superiorhealthplan.com	sara.pena@superiorhealthplan.com	Sara	Pena		Health Plan Employee
evett.bayles@superiorhealthplan.com	evett.bayles@superiorhealthplan.com	Evett	Bayles		Health Plan Employee
maryann.haddad@superiorhealthplan.com	maryann.haddad@superiorhealthplan.com	Mary Ann	Haddad		Health Plan Employee
chartaimer.mcqueen@superiorhealthplan.com	chartaimer.mcqueen@superiorhealthplan.com	Chartaimer	McQueen		Health Plan Employee
micah.smith@superiorhealthplan.com	micah.smith@superiorhealthplan.com	Micah	Smith		Health Plan Employee
colleen.gossling@superiorhealthplan.com	colleen.gossling@superiorhealthplan.com	Colleen	Gossling		Health Plan Employee
lspence@hslawmail.com	lspence@hslawmail.com	Logan	Spence		Health Plan Contract Lobbyist
emily.elizarde@superiorhealthplan.com	emily.elizarde@superiorhealthplan.com	Emily	Elizarde		Health Plan Employee
karen.f.blizzardmarsh@superiorhealthplan.com	karen.f.blizzardmarsh@superiorhealthplan.com	Karen	Blizzard		Health Plan Employee
arnulfo.rios@superiorhealthplan.com	arnulfo.rios@superiorhealthplan.com	Arnulfo	Rios		Health Plan Employee
valerie.chapa@superiorhealthplan.com	valerie.chapa@superiorhealthplan.com	Valerie	Chapa		Health Plan Employee
kathleen.ballee@superiorhealthplan.com	kathleen.ballee@superiorhealthplan.com	Kathy	Ballee		Health Plan Employee
jessica.najera@superiorhealthplan.com	jessica.najera@superiorhealthplan.com	Jessica	Najera		Health Plan Employee
andrea.gillentine@superiorhealthplan.com	andrea.gillentine@superiorhealthplan.com	Andrea	Gillentine		Health Plan Employee
andrea.brambila@superiorhealthplan.com	andrea.brambila@superiorhealthplan.com	Andrea	Brambila		Health Plan Employee
orlando.julian@superiorhealthplan.com	orlando.julian@superiorhealthplan.com	Orlando	Juilan		Health Plan Employee
valerie.gates@superiorhealthplan.com	valerie.gates@superiorhealthplan.com	Valerie	Gates		Health Plan Employee
porcha.pulley@superiorhealthplan.com	porcha.pulley@superiorhealthplan.com	Porcha	Pulley		Health Plan Employee
jennifer.alanis@superiorhealthplan.com	jennifer.alanis@superiorhealthplan.com	Jennifer	Alanis		Health Plan Employee
stan@schluetergroup.com	stan@schluetergroup.com	Stan	Schlueter		Health Plan Contract Lobbyist
veronica.laduc@superiorhealthplan.com	veronica.laduc@superiorhealthplan.com	Veronica	LaDuc		Health Plan Employee
kenneth.james@superiorhealthplan.com	kenneth.james@superiorhealthplan.com	Kenneth	James		Health Plan Employee
ryan.mckenna@superiorhealthplan.com	ryan.mckenna@superiorhealthplan.com	Ryan	McKenna		Health Plan Employee
thomas.nguyen@superiorhealthplan.com	thomas.nguyen@superiorhealthplan.com	Thomas	Nguyen		Health Plan Employee
brad@schluetergroup.com	brad@schluetergroup.com	Brad	Schlueter		Health Plan Contract Lobbyist
holly.munin@superiorhealthplan.com	holly.munin@superiorhealthplan.com	Holly	Munin		Health Plan Employee
verna.pratt@superiorhealthplan.com	verna.pratt@superiorhealthplan.com	Verna	Pratt		Health Plan Employee
robert.wilson@superiorhealthplan.com	robert.wilson@superiorhealthplan.com	Robert K.	Wilson		Health Plan Employee
ceseley.rollins@superiorhealthplan.com	ceseley.rollins@superiorhealthplan.com	Ceseley	Rollins		Health Plan Employee
troy.riley@superiorhealthplan.com	troy.riley@superiorhealthplan.com	Troy	Riley		Health Plan Employee
david.harmon@superiorhealthplan.com	david.harmon@superiorhealthplan.com	David	Harmon		Health Plan Employee
charles.dubose@superiorhealthplan.com	charles.dubose@superiorhealthplan.com	Charles	DuBose		Health Plan Employee
michael.cation@superiorhealthplan.com	michael.cation@superiorhealthplan.com	Michael	Cation		Health Plan Employee
ryan.link@centene.com	ryan.link@centene.com	Ryan	Link		Health Plan Employee
jason.mcbride@superiorhealthplan.com	jason.mcbride@superiorhealthplan.com	Jason	McBride		Health Plan Employee
jeremy.lloyd@superiorhealthplan.com	jeremy.lloyd@superiorhealthplan.com	Jeremy	Lloyd		Health Plan Employee
twise@centene.com	twise@centene.com	Tom	Wise		Health Plan Employee
francie.wambua@superiorhealthplan.com	francie.wambua@superiorhealthplan.com	kalunde	wambua		Health Plan Employee
amy.meyers@superiorhealthplan.com	amy.meyers@superiorhealthplan.com	Amy	Meyers		Health Plan Employee
tammy.c.edwards@centene.com	tammy.c.edwards@centene.com	Tammy	Edwards		Health Plan Employee
kia.biller@superiorhealthplan.com	kia.biller@superiorhealthplan.com	Kia	Biller		Health Plan Employee
cynthia.rojas@superiorhealthplan.com	cynthia.rojas@superiorhealthplan.com	Cynthia	Rojas		Health Plan Employee
michelle.fouche@superiorhealthplan.com	michelle.fouche@superiorhealthplan.com	Michelle	Fouche		Health Plan Employee
sarah.esquivel@superiorhealthplan.com	sarah.esquivel@superiorhealthplan.com	sarah	esquivel		Health Plan Employee
lesa.warren@superiorhealthplan.com	lesa.warren@superiorhealthplan.com	Lesa	Warren		Health Plan Employee
sarah.sorensen@superiorhealthplan.com	sarah.sorensen@superiorhealthplan.com	Sarah	Sorensen		Health Plan Employee
robert.wilson@superiorhealthplan.com	robert.wilson@superiorhealthplan.com	Robert	Wilson		Health Plan Employee
vicki.estrada@superiorhealthplan.com	vicki.estrada@superiorhealthplan.com	Vicki	Estrada		Health Plan Employee
rachael.przybyla@superiorhealthplan.com	rachael.przybyla@superiorhealthplan.com	rachael	przybyla		Health Plan Employee
michael.diel@superiorhealthplan.com	michael.diel@superiorhealthplan.com	Michael	Diel		Health Plan Employee
natalie.hernandez@superiorhealthplan.com	natalie.hernandez@superiorhealthplan.com	Natalie	Hernandez		Health Plan Employee
jessica.estrada@superiorhealthplan.com	jessica.estrada@superiorhealthplan.com	Jessica	Estrada		Health Plan Employee
jonathan.gallop@superiorhealthplan.com	jonathan.gallop@superiorhealthplan.com	Jonahan	Gallop		Health Plan Employee
jennifer.e.nehrkorn@superiorhealthplan.com	jennifer.e.nehrkorn@superiorhealthplan.com	Jenniver	Nehrkorn		Health Plan Employee
kcalvert@centene.com	kcalvert@centene.com	Kevin	Calvert		Health Plan Employee
noemi.smithroat@superiorhealthplan.com	noemi.smithroat@superiorhealthplan.com	Noemi	Smithroat		Health Plan Employee
Taylor.Cooper@CENTENE.COM	Taylor.Cooper@CENTENE.COM	Taylor	Cooper		Health Plan Employee
Saul.Ortega@superiorhealthplan.com	Saul.Ortega@superiorhealthplan.com	Saul	Ortega		Health Plan Employee
marina.fahim@superiorhealth.com	marina.fahim@superiorhealth.com	Marina	fahim		Health Plan Employee
Katheryn.Johnson@superiorhealthplan.com	Katheryn.Johnson@superiorhealthplan.com	Katheryn	Johnson		Health Plan Employee
gavin@gavinmassingill.com	gavin@gavinmassingill.com	Gavin	Massingill		Health Plan Employee
Teresa.Gonzales@superiorhealthplan.com	Teresa.Gonzales@superiorhealthplan.com	Teresa	Gonzales		Health Plan Employee
Nicole.M.Hoffman@superiorhealthplan.com	Nicole.M.Hoffman@superiorhealthplan.com	Nicole	Hoffman		Health Plan Employee
Nathan.Hoover@superiorhealthplan.com	Nathan.Hoover@superiorhealthplan.com	Nathan	Hoover		Health Plan Employee
Dan.Horn@superiorhealthplan.com	Dan.Horn@superiorhealthplan.com	Dan	Horn		Health Plan Employee
dana.chothmounethinh@superiorhealthplan.com	dana.chothmounethinh@superiorhealthplan.com	Dana	Chothmounethinh		Health Plan Employee
Michelle.Szymanski@superiorhealthplan.com	Michelle.Szymanski@superiorhealthplan.com
jared.wolfe@superiorhealthplan.com	jared.wolfe@superiorhealthplan.com	Jared	Wolfe		Health Plan Employee
mark.sanders@superiorhealthplan.com	mark.sanders@superiorhealthplan.com	Mark	Sanders		Health Plan Employee
karen.cheng@superiorhealthplan.com	karen.cheng@superiorhealthplan.com	Karen	Cheng		Health Plan Employee
chuck.hopson@superiorhealthplan.com	chuck.hopson@superiorhealthplan.com	Chuck	Hopson		Health Plan Employee
eric.glenn@superiorhealthplan.com	eric.glenn@superiorhealthplan.com	ERIC	GLENN		Health Plan Employee
drew@lawsonstrategies.com	drew@lawsonstrategies.com	Drew	Lawson		Health Plan Contract Lobbyist
casey@blakemore.us	casey@blakemore.us	Casey	Haney		Health Plan Contract Lobbyist
eddie@luciolegal.com	eddie@luciolegal.com	Eddie	Lucio		Health Plan Contract Lobbyist
Billy@billyphenix.com	Billy@billyphenix.com	Billy	Phenix		Health Plan Contract Lobbyist
Will@billyphenix.com	Will@billyphenix.com	Will	Temple		Health Plan Contract Lobbyist
revcobob@gmail.com	revcobob@gmail.com	Robert	Haney		Health Plan Contract Lobbyist
keith@bnsfirm.com	keith@bnsfirm.com	Keith	Strama		Health Plan Contract Lobbyist
meason@tahp.org	meason@tahp.org	Melissa	Eason		Health Plan Employee
kjones@taihooncology.com	kjones@taihooncology.com	Kurt	Jones		Affiliate
lisa@daviskaufman.com	lisa@daviskaufman.com	Lisa	Kaufman		Health Plan Contract Lobbyist
denise@daviskaufman.com	denise@daviskaufman.com	Denise	Davis		Health Plan Contract Lobbyist
wendy@daviskaufman.com	wendy@daviskaufman.com	Wendy	Wilson		Health Plan Contract Lobbyist
jill.melton@tachp.org	jill.melton@tachp.org	Jill	Melton		Health Plan Employee
rose@rahconsulting.com	rose@rahconsulting.com	Rose	Hayden		Health Plan Contract Lobbyist
kay.ghahremani@tachp.org	kay.ghahremani@tachp.org	Kay	Ghahremani		Health Plan Employee
eawillia@texaschildrens.org	eawillia@texaschildrens.org	Eric	Williams		Health Plan Employee
pcpeter@texaschildrens.org	pcpeter@texaschildrens.org	Peter	Peter		Health Plan Employee
pmhsing@texaschildrens.org	pmhsing@texaschildrens.org	Patricia	Hsing		Health Plan Employee
ebalvara@texaschildrens.org	ebalvara@texaschildrens.org	Erika	Alvarado		Health Plan Employee
mwmullar@texaschildrens.org	mwmullar@texaschildrens.org	Mark	Mullarkey		Health Plan Employee
bsbabber@texaschildrens.org	bsbabber@texaschildrens.org	Bhavana	Babber		Health Plan Employee
kdbutler@texaschildrens.org	kdbutler@texaschildrens.org	Katara	Butler		Health Plan Employee
kkosterm@texaschildrens.org	kkosterm@texaschildrens.org	Katy	Ostermaier		Health Plan Employee
cmhicks@texaschildrens.org	cmhicks@texaschildrens.org	Christi	Hicks		Health Plan Employee
dhscardi@texaschildrens.org	dhscardi@texaschildrens.org	Diane	Scardino		Health Plan Employee
tmdewey@texaschildrens.org	tmdewey@texaschildrens.org	Tina	Dewey		Health Plan Employee
agsimms@texaschildrens.org	agsimms@texaschildrens.org	Ashley	Simms		Health Plan Employee
vawoznia@texaschildrens.org	vawoznia@texaschildrens.org	Vivian	Wozniak		Health Plan Employee
smkim1@texaschildrens.org	smkim1@texaschildrens.org	Stella	Kim		Health Plan Employee
vkparson@texaschildrens.org	vkparson@texaschildrens.org	Veronic	Parson		Health Plan Employee
jjingram@texaschildrens.org	jjingram@texaschildrens.org	Jackie	Ingram		Health Plan Employee
bdlee@texaschildrens.org	bdlee@texaschildrens.org	Barbara	Lee		Health Plan Employee
txbarne1@texaschildrens.org	txbarne1@texaschildrens.org	Tanya	Barnes		Health Plan Employee
egcolvin@texaschildrens.org	egcolvin@texaschildrens.org	Elisha	Colvin		Health Plan Employee
aebriley@texaschildrens.org	aebriley@texaschildrens.org	Amy	Briley		Health Plan Employee
KALEMMER@texaschildrens.org	KALEMMER@texaschildrens.org	Kristi	Lemmert		Health Plan Employee
snalliso@texaschildrens.org	snalliso@texaschildrens.org	Sebrina	Allison		Health Plan Employee
axleeper@texaschildrens.org	axleeper@texaschildrens.org	Audrianna	Leeper		Health Plan Employee
jxbritto@texaschildrens.org	jxbritto@texaschildrens.org	Jana	Britton		Health Plan Employee
mhhill@texaschildrens.org	mhhill@texaschildrens.org	Marian (Manny)	Hill		Health Plan Employee
onwagner@texaschildrens.org	onwagner@texaschildrens.org	Opera	Wagner-Ross		Health Plan Employee
rxfleisc@texaschildrens.org	rxfleisc@texaschildrens.org	Richelle	Fleischer		Health Plan Employee
mxmurph4@texaschildrens.org	mxmurph4@texaschildrens.org	Michael	Murphy		Health Plan Employee
kehill1@texaschildrens.org	kehill1@texaschildrens.org	Karen	Hill		Health Plan Employee
mrcooke@texaschildrens.org	mrcooke@texaschildrens.org	Meredith	Cooke		Health Plan Employee
jlcarls1@texaschildrens.org	jlcarls1@texaschildrens.org	Johnna	Carlson		Health Plan Employee
smsmithe@texaschildrens.org	smsmithe@texaschildrens.org	Shantelle	Smither		Health Plan Employee
asriggs@texaschildrens.org	asriggs@texaschildrens.org	April	Riggs		Health Plan Employee
jnorton@texasmutual.com	jnorton@texasmutual.com	Jo Betsy	Norton		Affiliate
paulschlaud@texasmutual.com	paulschlaud@texasmutual.com	Paul	Schlaud		Affiliate
KWirsig@txmholdings.com	KWirsig@txmholdings.com	Kellie	Wirsig		Health Plan Employee
MDuncan@txmholdings.com	MDuncan@txmholdings.com	Meredith	Duncan		Health Plan Employee
chad@texasstaralliance.com	chad@texasstaralliance.com	Chad	Cantella		Professional Affiliate
ryan@texasstaralliance.com	ryan@texasstaralliance.com	Ryan	Clay		Professional Affiliate
lucinda@texasstaralliance.com	lucinda@texasstaralliance.com	Lucinda	Saxon		Professional Affiliate
annie.nabers@thsa.org	annie.nabers@thsa.org	Annie	Nabers		Affiliate
george.gooch@thsa.org	george.gooch@thsa.org	George	Gooch		Affiliate
eric.heflin@thsa.org	eric.heflin@thsa.org	Eric	Heflin		Affiliate
sarah@treatyoakstrategies.com	sarah@treatyoakstrategies.com	Sarah	Mills		Health Plan Contract Lobbyist
laurie@treatyoakstrategies.com	laurie@treatyoakstrategies.com	Laurie	Vanhoose		Health Plan Contract Lobbyist
heather.durst@ucb.com	heather.durst@ucb.com	Heather	Durst		Affiliate
hope.berry@ucb.com	hope.berry@ucb.com	Hope	Berry		Affiliate
amy.whited@ucb.com	amy.whited@ucb.com	Amy	Whited		Affiliate
dfick@uhc.com	dfick@uhc.com	Dave	Fick		Associate
ankit.amin@uhc.com	ankit.amin@uhc.com	Ankit	Amin		Associate
jillian_hamblin@uhc.com	jillian_hamblin@uhc.com	Jillian	Hamblin		Health Plan Employee
deborah_l_bond@uhc.com	deborah_l_bond@uhc.com	Deborah	Bond		Associate
patricia_logan@uhc.com	patricia_logan@uhc.com	Patty	Logan		Associate
michelle.c.miller@uhc.com	michelle.c.miller@uhc.com	Michelle	Miller		Associate
angel.encinas@uhc.com	angel.encinas@uhc.com	Angel	Encinas		Associate
lsalcedo@uhc.com	lsalcedo@uhc.com	Laura	Salcedo		Associate
mary_e_voysest@uhc.com	mary_e_voysest@uhc.com	Mary	Voysest		Associate
kelly_j_risch@uhc.com	kelly_j_risch@uhc.com	Kelly	Risch		Associate
zena.oshiro@uhc.com	zena.oshiro@uhc.com	Zena	Oshiro		Associate
mguillory@umojasupply.com	mguillory@umojasupply.com	Megan	Guillory		Affiliate
holly_hannes@uhc.com	holly_hannes@uhc.com	Holly	Hannes		Health Plan Employee
davidsolyom@uhc.com	davidsolyom@uhc.com	David	Solyom		Health Plan Employee
nmeier@uhc.com	nmeier@uhc.com	Nneka	Meier		Health Plan Employee
johnathan_leonard@uhc.com	johnathan_leonard@uhc.com	Johnathan	Leonard		Health Plan Employee
judi_shaw-rice@uhc.com	judi_shaw-rice@uhc.com	Judi	Shaw-Rice		Health Plan Employee
jazmin_elizondo@uhc.com	jazmin_elizondo@uhc.com	Jazmin	Elizondo		Health Plan Employee
maria_g_shydlo@uhc.com	maria_g_shydlo@uhc.com	Maria	Gordon Shydlo		Health Plan Employee
jeanne_m_cavanaugh@uhc.com	jeanne_m_cavanaugh@uhc.com	Jeanne	Cavanaugh		Health Plan Employee
ginger_l_wommack@uhc.com	ginger_l_wommack@uhc.com	Ginger	Wommack		Health Plan Employee
stephanie_n_vanarsdale@uhc.com	stephanie_n_vanarsdale@uhc.com	Stephanie	Vanarsdale		Health Plan Employee
glenda_l_coleman@uhc.com	glenda_l_coleman@uhc.com	Glenda	Coleman		Health Plan Employee
lara@txlobby.com	lara@txlobby.com	Lara	Keel		Health Plan Contract Lobbyist
tiffany_handshy@uhc.com	tiffany_handshy@uhc.com	Tiffany	Handshy		Health Plan Employee
desiree.melching@uhc.com	desiree.melching@uhc.com	Desiree	Melching		Health Plan Employee
kristie_l_walker@uhc.com	kristie_l_walker@uhc.com	Kristie	Walker		Health Plan Employee
arnita_burton@uhc.com	arnita_burton@uhc.com	Arnita	Burton		Health Plan Employee
ellen.obrien@uhc.com	ellen.obrien@uhc.com	Ellen	OBrien		Health Plan Employee
tamika_l_nolen@uhc.com	tamika_l_nolen@uhc.com	Tamika	Nolen		Health Plan Employee
sdeshpande@uhc.com	sdeshpande@uhc.com	Salil	Deshpande		Health Plan Employee
kirk.zihlman@uhc.com	kirk.zihlman@uhc.com	Kirk	Zihlman		Health Plan Employee
jeffrey.rayl@uhc.com	jeffrey.rayl@uhc.com	Jeff	Rayl		Health Plan Employee
eyitoyosi_akuchie@uhc.com	eyitoyosi_akuchie@uhc.com	Eyitoyosi	Akuchie		Health Plan Employee
david_k_hill@uhc.com	david_k_hill@uhc.com	David	Hill		Health Plan Employee
tracy.okolo@uhc.com	tracy.okolo@uhc.com	Tracy	Okolo		Health Plan Employee
tanya.a.roberts@uhc.com	tanya.a.roberts@uhc.com	Tanya	Roberts		Health Plan Employee
julie_b_garcia@uhc.com	julie_b_garcia@uhc.com	Julie	Garcia		Health Plan Employee
ginna_wilson@uhc.com	ginna_wilson@uhc.com	Ginna	Wilson		Health Plan Employee
mei_ling_christopher@uhc.com	mei_ling_christopher@uhc.com	Mei	Christopher		Health Plan Employee
meka_n_lasalle@uhc.com	meka_n_lasalle@uhc.com	Meka	LaSalle		Health Plan Employee
joe_bedford@uhc.com	joe_bedford@uhc.com	Joe	Bedford		Health Plan Employee
john_c_guedry@uhc.com	john_c_guedry@uhc.com	John	Guedry		Health Plan Employee
lcalo@uhc.com	lcalo@uhc.com	Luis	Calo		Health Plan Employee
angela_l_young@uhc.com	angela_l_young@uhc.com	Angela	Young		Health Plan Employee
lisa_k_reuter@uhc.com	lisa_k_reuter@uhc.com	Lisa	Reuter		Health Plan Employee
joe_trevino@uhc.com	joe_trevino@uhc.com	Joe	Trevino		Health Plan Employee
juan_c_osorio@uhc.com	juan_c_osorio@uhc.com	Juan	Osorio		Health Plan Employee
gena_r_jongebloed@uhc.com	gena_r_jongebloed@uhc.com	Gena	Jongebloed		Health Plan Employee
megan_haddock@uhc.com	megan_haddock@uhc.com	Megan	Haddock		Health Plan Employee
erica@epsconsulting.net	erica@epsconsulting.net	Erica	Stick		Health Plan Contract Lobbyist
jeri_applegate@uhc.com	jeri_applegate@uhc.com	Jeri	Applegate		Health Plan Employee
mary.l.henry-zeek@uhc.com	mary.l.henry-zeek@uhc.com	Mary	Henry-Zeek		Health Plan Employee
kristina.suberbielle@uhc.com	kristina.suberbielle@uhc.com	Kristina	Suberbielle		Health Plan Employee
angela_trahan@uhc.com	angela_trahan@uhc.com	Angela	Trahan		Health Plan Employee
yvette_r_wolfe@uhc.com	yvette_r_wolfe@uhc.com	Yvette	Wolfe		Health Plan Employee
deborah_l_deska@uhc.com	deborah_l_deska@uhc.com	Deborah	Deska		Health Plan Employee
sharmae_m_erickson@uhc.com	sharmae_m_erickson@uhc.com	Sharmae	Erickson		Health Plan Employee
morgan.k.galow@uhc.com	morgan.k.galow@uhc.com	Morgan	Galow		Health Plan Employee
rachana_patwa@uhc.com	rachana_patwa@uhc.com	Rachana	Patwa		Health Plan Employee
david_milich@uhc.com	david_milich@uhc.com	David	Milich		Health Plan Employee
christina_murphy@uhc.com	christina_murphy@uhc.com	Christina	Murphy		Health Plan Employee
christi_wondrash@uhc.com	christi_wondrash@uhc.com	Christi	Wondrash		Health Plan Employee
maria_d_moreland@uhc.com	maria_d_moreland@uhc.com	Maria	Moreland		Health Plan Employee
patricia_l_cobb@uhc.com	patricia_l_cobb@uhc.com	Patricia	Cobb		Health Plan Employee
lauren_a_caddell@uhc.com	lauren_a_caddell@uhc.com	Lauren	Caddell		Health Plan Employee
mandie.eichenlaub@uhc.com	mandie.eichenlaub@uhc.com	Mandie	Eichenlaub		Health Plan Employee
marshall_dawer@uhc.com	marshall_dawer@uhc.com	Marshall	Dawer		Health Plan Employee
kimberly_campbell@uhc.com	kimberly_campbell@uhc.com	Kimberly	Campbell		Health Plan Employee
stephanie_villarreal@uhc.com	stephanie_villarreal@uhc.com	Stephanie	Villarreal		Health Plan Employee
karen_howard@uhc.com	karen_howard@uhc.com	Karen	Howard		Health Plan Employee
tammie_l_rogers@uhc.com	tammie_l_rogers@uhc.com	Tammie	Rogers		Health Plan Employee
otaresiri_l_inije@uhc.com	otaresiri_l_inije@uhc.com	Otaresiri Lorraine	Inije		Health Plan Employee
srverratti@uhc.com	srverratti@uhc.com	Shelbi	Verratti		Health Plan Employee
elizabeth_lamair@uhc.com	elizabeth_lamair@uhc.com	Elizabeth	Lamiar		Health Plan Employee
lindsey_farley@uhc.com	lindsey_farley@uhc.com	Lindsey	Farley		Health Plan Employee
caitlyn.maccollum@uhc.com	caitlyn.maccollum@uhc.com	Caitlyn	Maccollum		Health Plan Employee
sonal_shah@uhc.com	sonal_shah@uhc.com	Sonal	Shah		Health Plan Employee
kristie_k_young@uhc.com	kristie_k_young@uhc.com	Kristie	Young		Health Plan Employee
bobbie_j_salinas@uhc.com	bobbie_j_salinas@uhc.com	Bobbie	Salinas		Health Plan Employee
alison_f_garton@uhc.com	alison_f_garton@uhc.com	Alison	Garton		Health Plan Employee
Jenniferrodriguez@me.com	Jenniferrodriguez@me.com	Jennifer	Rodriguez		Health Plan Contract Lobbyist
marc@marctx.com	marc@marctx.com	Marc	Rodriquez		Health Plan Contract Lobbyist
chrisrtraylor@gmail.com	chrisrtraylor@gmail.com	Chris	Traylor		Health Plan Contract Lobbyist
linda.l.baker@uhc.com	linda.l.baker@uhc.com	Linda	Baker		Health Plan Employee
mary_h_beery@uhc.com	mary_h_beery@uhc.com	Mary	Beery		Health Plan Employee
brandy@brandymarquez.com	brandy@brandymarquez.com	Brandy	Marty		Health Plan Employee
karla_mione@uhc.com	karla_mione@uhc.com	Karla	Mione		Health Plan Employee
gregg_sherrill@uhc.com	gregg_sherrill@uhc.com				Health Plan Employee
caren_zysk@uhc.com	caren_zysk@uhc.com	Caren	Zysk		Health Plan Employee
susan_brunes@uhc.com	susan_brunes@uhc.com	Susan	Brunes		Health Plan Employee
shauna_ewing@uhc.com	shauna_ewing@uhc.com	Shauna	Ewing		Health Plan Employee
diane_kochol@uhc.com	diane_kochol@uhc.com	Diane	Kochol		Health Plan Employee
Susan_Brunes@uhc.com	Susan_Brunes@uhc.com	Susan	Brunes		Health Plan Employee
jeffrey_maddox@uhc.com	jeffrey_maddox@uhc.com	Jeff	Maddox		Health Plan Employee
scott_flannery@uhc.com	scott_flannery@uhc.com	Scott	Flannery		Health Plan Employee
chris_cronn@uhg.com	chris_cronn@uhg.com	Chris	Cronn		Health Plan Employee
marian_cabanillas@uhc.com	marian_cabanillas@uhc.com	Marian	Cabanillas		Health Plan Employee
don_langer@uhc.com	don_langer@uhc.com	Don	Langer		Health Plan Employee
patricia_camacho-longoria@uhc.com	patricia_camacho-longoria@uhc.com	Patricia	Longoria		Health Plan Employee
bernie_inskeep@uhc.com	bernie_inskeep@uhc.com	Bernie	Inskeep		Health Plan Employee
brett_m_edwards@uhc.com	brett_m_edwards@uhc.com	Brett	Edwards		Health Plan Employee
alisa.lotrakul@uhc.com	alisa.lotrakul@uhc.com	Alisa	Lotrakul		Health Plan Employee
addover@usablemutual.com	addover@usablemutual.com	Angela	Dover		Health Plan Employee
tggauger@usablemutual.com	tggauger@usablemutual.com	Tim	Gauger		Health Plan Employee
dwfrazier@arkbluecross.com	dwfrazier@arkbluecross.com	David	Frazier		Health Plan Employee
mrmartin@arkbluecross.com	mrmartin@arkbluecross.com	Michael	Martin		Health Plan Employee
vkwoods@arkbluecross.com	vkwoods@arkbluecross.com	Veronica	Woods		Health Plan Employee
bkdorathy@arkbluecross.com	bkdorathy@arkbluecross.com	Bryan	Dorathy		Health Plan Employee
cebarnett@arkbluecross.com	cebarnett@arkbluecross.com	Curtis	Barnett		Health Plan Employee
zachrisman@usablemutual.com	zachrisman@usablemutual.com	Zane	Chrisman		Health Plan Employee
majames@arkbluecross.com	majames@arkbluecross.com	Marcus	James		Health Plan Employee
skstanley@usablemutual.com	skstanley@usablemutual.com	Sarah	Stanley		Health Plan Employee
jdtreece@arkbluecross.com	jdtreece@arkbluecross.com	Jason	Treece		Health Plan Employee
mcdodson@usablemutual.com	mcdodson@usablemutual.com	Chad	Dodson		Health Plan Employee
aecates@arkbluecross.com	aecates@arkbluecross.com	Anita	Cates		Health Plan Employee
fbsewall@usablemutual.com	fbsewall@usablemutual.com	Frank	Sewall		Health Plan Employee
cmkittler@usablemutual.com	cmkittler@usablemutual.com	Christi	Kittler		Health Plan Employee
srobinson@valuehealth.com	srobinson@valuehealth.com	S.	Robinson		Affiliate
tmattingly@valuehealth.com	tmattingly@valuehealth.com	Tom	Mattingly		Affiliate
rfowle@valuehealth.com	rfowle@valuehealth.com	Robert	Fowle		Affiliate
david.dunbar@versanthealth.com	david.dunbar@versanthealth.com	David	Dunbar		Affiliate
megan.ryczek@versanthealth.com	megan.ryczek@versanthealth.com	Megan	Ryczek		Affiliate
courtney.jonesduggan@versanthealth.com	courtney.jonesduggan@versanthealth.com	Courtney	Duggan		Affiliate
lisa.olexy@versanthealth.com	lisa.olexy@versanthealth.com	Lisa	Olexy		Affiliate
vaughn.koter@versanthealth.com	vaughn.koter@versanthealth.com	Vaughn	Koter		Affiliate
Danielle.Angel@versanthealth.com	Danielle.Angel@versanthealth.com	Danielle	Angel		Affiliate
beth.rossi@wildbluehealthsolutions.com	beth.rossi@wildbluehealthsolutions.com	Beth	Rossi		Professional Affiliate
ken.janda@wildbluehealthsolutions.com	ken.janda@wildbluehealthsolutions.com	Ken	Janda		Professional Affiliate
daniel.crowe@wildbluehealthsolutions.com	daniel.crowe@wildbluehealthsolutions.com	Daniel	Crowe		Professional Affiliate
bcatano@winstead.com	bcatano@winstead.com	Beatriz	Catano		Professional Affiliate
aharvey@winstead.com	aharvey@winstead.com	Amanda	Harvey		Professional Affiliate
crupprath@winstead.com	crupprath@winstead.com	Carrie	Rupprath		Professional Affiliate
jloehr@winstead.com	jloehr@winstead.com	Jacob	Loehr		Professional Affiliate
gorr@zeomega.com	gorr@zeomega.com	Gus	Orr		Affiliate
mhopper@zeomega.com	mhopper@zeomega.com	Mary	Hopper		Affiliate
shameet@vheda.com	shameet@vheda.com	shameet	Luhar		Affiliate
david.williams@podimetrics.com	david.williams@podimetrics.com	David	Williams
lori.howarth@bayer.com	lori.howarth@bayer.com	Lori	Howarth
cindy.buckels@rightsitehealth.com	cindy.buckels@rightsitehealth.com	Cindy	Buckels
edalexander@goodrootinc.com	edalexander@goodrootinc.com	Emily	D'Alexander
rcipriano@scene.health	rcipriano@scene.health	Rachel	Cipriano
blovely@hhaexchange.com	blovely@hhaexchange.com	Barbara	Lovely
smcleod@itilitiheatlh.com	smcleod@itilitiheatlh.com	Steve	McLeod
payal.parekh@phhs.org	payal.parekh@phhs.org	Payal	Parekh		Health Plan Employee
j_allison_grant@uhc.com	j_allison_grant@uhc.com	Allison	Grant
jennifer_a_saenz@uhc.com	jennifer_a_saenz@uhc.com	Jennifer	Saenz
Adelaida.Corral@alivi.com	Adelaida.Corral@alivi.com	Adelaida	Corral
dstreeter@caqh.org	dstreeter@caqh.org	David	Streeter
caroline.seeley@carebridgehealth.com	caroline.seeley@carebridgehealth.com	Caroline	Seeley
cassandra.mendenhall@organon.com	cassandra.mendenhall@organon.com	Cassandra	Mendenhall
katherina.tinney@organon.com	katherina.tinney@organon.com	Katie	tinney
lisa.davis2@organon.com	lisa.davis2@organon.com	Lisa	Davis
adelaida.corral@alivi.com	adelaida.corral@alivi.com	Adelaida	Corral
johnathan.gallop@superiorhealthplan.com	johnathan.gallop@superiorhealthplan.com	Johnathan	Gallop
nathan.hoover@superiorhealthplan.com	nathan.hoover@superiorhealthplan.com	Nathan	Hoover
shari_waldie@bcbstx.com	shari_waldie@bcbstx.com	Shari	Waldie		Health Plan Employee
jason.gajewski@superiorhealthplan.com	jason.gajewski@superiorhealthplan.com	Jason	Gajewski
cheryl.d.rhines@superiorhealthplan.com	cheryl.d.rhines@superiorhealthplan.com	DENECE	RHINES
jennifer.houston@superiorhealthplan.com	jennifer.houston@superiorhealthplan.com	Jennifer	Houston
maria.elizarde@superiorhealthplan.com	maria.elizarde@superiorhealthplan.com	Emily	Elizarde
leticia.espiritu@superiorhealthplan.com	leticia.espiritu@superiorhealthplan.com	Letty	Ontiveros
twinn@superiorhealthplan.com	twinn@superiorhealthplan.com	Thelma	Winn
Dominic.Weilbaecher@babsondx.com	Dominic.Weilbaecher@babsondx.com	Dominic	Weilbaecher
chuck.grabow@superiorhealthplan.com	chuck.grabow@superiorhealthplan.com	Chuck	Grabow
Tessa.Perez@dchstx.org	Tessa.Perez@dchstx.org	Tessa	Perez		Health Plan Employee
alex.sommer@avalonhcs.com	alex.sommer@avalonhcs.com	Alex	Sommer
joel.meyer@novartis.com	joel.meyer@novartis.com	Joel	Meyer
christy.gustafson@superiorhealthplan.com	christy.gustafson@superiorhealthplan.com	Christy	Gustafson
brad.clay@novartis.com	brad.clay@novartis.com	Brad	Clay
alan.picard@novartis.com	alan.picard@novartis.com	Alan	Picard
mai.duong@novartis.com	mai.duong@novartis.com	Mai	Duong
melissa.deep@emcarahealth.com	melissa.deep@emcarahealth.com	Melissa	Deep
Heather_R_Martinez@bcbstx.com	Heather_R_Martinez@bcbstx.com	Heather	Martinez		Health Plan Employee
mcostello@dsswtx.org	mcostello@dsswtx.org	Marjorie	Costello
kjeffrey@cdsintexas.com	kjeffrey@cdsintexas.com	Kevin	Jeffrey
abaker@cdsintexas.com	abaker@cdsintexas.com	April	Baker
lnbaker@cdsintexas.com	lnbaker@cdsintexas.com	Lawrence	Baker
KIMBERLY.AARON@COOKCHILDRENS.ORG	KIMBERLY.AARON@COOKCHILDRENS.ORG	Kimberly	Aaron		Health Plan Employee
Teresa.gonzales@superiorhealthplan.com	Teresa.gonzales@superiorhealthplan.com	Teresa	Gonzales
nikki.lobdell@cookchildrens.org	nikki.lobdell@cookchildrens.org	Nikki	Lobdell		Health Plan Employee
heather.korbulic@getinsured.com	heather.korbulic@getinsured.com	Heather	Korbulic		Affiliate
paul.neutz@getinsured.com	paul.neutz@getinsured.com	Paul	Neutz
lauraslawlor@gmail.com	lauraslawlor@gmail.com	Laura	Lawlor
julia.figueroa2@superiorhealthplan.com	julia.figueroa2@superiorhealthplan.com	Julia	Figueroa
testuser@tester.com	testuser@tester.com	Berg	Berg		PBM Contract Lobbyist
testnewsuserfast@test.com	testnewsuserfast@test.com	test new	user		PBM Contract Lobbyist
Bergan00@gmail.com	Bergan00@gmail.com	Bergan	test		Associate
CMHicks@texaschildrens.org	CMHicks@texaschildrens.org	Christi	Hicks
kxscottg@texaschildrens.org	kxscottg@texaschildrens.org	Kathy	Scott-Gurnell
eeanders@texaschildrens.org	eeanders@texaschildrens.org	Eric	Anderson
lrfulle1@texaschildrens.org	lrfulle1@texaschildrens.org	Lisa	Fuller
Lauren.Rios@dchstx.org	Lauren.Rios@dchstx.org	Lauren	Rios
Marcy.dickson@molinahealthcare.com	Marcy.dickson@molinahealthcare.com	Marcy	Dickson
Elaine_Gold@bcbsil.com	Elaine_Gold@bcbsil.com	Elaine	Gold
leetagreer@gmail.com	leetagreer@gmail.com	Leeta	Greer
Rebecca.Solis@molinahealthcare.com	Rebecca.Solis@molinahealthcare.com	Rebecca	Solis
robin.reimschissel@molinahealthcare.com	robin.reimschissel@molinahealthcare.com	Robin	Reimschissel
edna.dudley@molinahealthcare.com	edna.dudley@molinahealthcare.com	Edna	Dudley
rachel.hopkins@molinahealthcare.com	rachel.hopkins@molinahealthcare.com	Rachel	Hopkins
Maria.Guerrero@Molinahealthcare.com	Maria.Guerrero@Molinahealthcare.com	Maria	Guerrero
Stephen.Bush@BSWHealth.org	Stephen.Bush@BSWHealth.org	Stephen	Bush		Health Plan Employee
Suzanne_Lakin@bcbstx.com	Suzanne_Lakin@bcbstx.com	Suzanne	Medrano
maren.peterson@uhc.com	maren.peterson@uhc.com	Maren	Peterson
wendy.mcgallion@molinahealthcare.come	wendy.mcgallion@molinahealthcare.come	Wendy	McGallion
cstephens@mcna.net	cstephens@mcna.net	Cheryl	Stephens
sharon.alvis@senderohealth.com	sharon.alvis@senderohealth.com	Sharon	Alvis		Health Plan Employee
nicole@curative.com	nicole@curative.com	Nicole	Ung		Health Plan Employee
madison.armbrester@carebridgehealth.com	madison.armbrester@carebridgehealth.com	Madison	Armbrester
sxsivert@texaschildrens.org	sxsivert@texaschildrens.org	Susan	Sivertsen
kari.suttee@novartis.com	kari.suttee@novartis.com	kari	suttee
neel.patel@phhs.org	neel.patel@phhs.org	Neel	Patel
weylieb@aetna.com	weylieb@aetna.com	Brian	Weylie
mayra_dominguez@uhc.com	mayra_dominguez@uhc.com	Mayra	Dominguez
sandi.howard@optum.com	sandi.howard@optum.com	Sandi	Howard
Ankit_x_patel@bcbsil.com	Ankit_x_patel@bcbsil.com	Ankit	Patel
Mark.Shaffer@Molinahealthcare.com	Mark.Shaffer@Molinahealthcare.com	Mark	Shaffer
yford@cfhp.com	yford@cfhp.com	Yadira	Ford
Teresa_Devine@bcbstx.com	Teresa_Devine@bcbstx.com	Teresa	Devine
leticia.ontiveros@superiorhealthplan.com	leticia.ontiveros@superiorhealthplan.com	Letty	Ontiveros
arnulfo.ramirez@dchstx.org	arnulfo.ramirez@dchstx.org	Arnulfo	Ramirez
DARWYN.WALKER@COOKCHILDRENS.ORG	DARWYN.WALKER@COOKCHILDRENS.ORG	Darwyn	Walker
Veronica.LaDuc@superiorhealthplan.com	Veronica.LaDuc@superiorhealthplan.com	Veronica	LaDuc
kandice.sanaie@cignahealthcare.com	kandice.sanaie@cignahealthcare.com	Kandice	Sanaie
amy.teske7@gmail.com	amy.teske7@gmail.com	Amy	Teske
maneesh.roberts@cookchildrens.org	maneesh.roberts@cookchildrens.org	Maneesh	Roberts
Felicia.Ramirez@phhs.org	Felicia.Ramirez@phhs.org	Felicia	Ramriez
yahaira.perez@cookchildrens.org	yahaira.perez@cookchildrens.org	YAHAIRA	PEREZ
Stephanie.Edwards@superiorhealthplan.com	Stephanie.Edwards@superiorhealthplan.com	Stephanie	Edwards
Erica.lerma@elpasohealth.com	Erica.lerma@elpasohealth.com	Erica	Mendez
jnorman@elpasohealth.com	jnorman@elpasohealth.com	Jourdan	Norman
rbarrozo@elpasohealth.com	rbarrozo@elpasohealth.com	Reynaldo	Barrozo
andersonc7@aetna.com	andersonc7@aetna.com	Chandra	Anderson
rebecca.stokes@Molinahealthcare.com	rebecca.stokes@Molinahealthcare.com	Rebecca	Stokes
Hochhaltera@aetna.com	Hochhaltera@aetna.com	Angie	Hochhalter
Barbara.stanley@superiorhealthplan.com	Barbara.stanley@superiorhealthplan.com	Barbara	Stanley
Robbin.Patton@cookchildrens.org	Robbin.Patton@cookchildrens.org	Robbin	Patton
nicole.gonzales2@molinahealthcare.com	nicole.gonzales2@molinahealthcare.com	Nicole	Gonzales
stacie.walkerposvar@bswhealth.org	stacie.walkerposvar@bswhealth.org	Stacie	Walker-Posvar
jasonleonwright@gmail.com	jasonleonwright@gmail.com	Jason	Wright
john.majors@bswhealth.org	john.majors@bswhealth.org	John	Majors
shyama.gandhi@molinahealthcare.com	shyama.gandhi@molinahealthcare.com	Shyama	Gandhi
jason.wright@phhs.org	jason.wright@phhs.org	Jason	Wright
christine.stivers@superiorhealthplan.com	christine.stivers@superiorhealthplan.com	Christine	Stivers
dee_cavaness@bcbstx.com	dee_cavaness@bcbstx.com	Dee	Cavaness
HarrisS16@aetna.com	HarrisS16@aetna.com	Sapheallah	Harris
kandice_walker@bcbstx.com	kandice_walker@bcbstx.com	Kandice	Walker
John_Sanchez@bcbstx.com	John_Sanchez@bcbstx.com	John	Sanchez
kunal_parekh@bcbsil.com	kunal_parekh@bcbsil.com	Kunal	Parekh
Janie_Park@bcbstx.com	Janie_Park@bcbstx.com	Janie	Park
exvillaf@texaschildrens.org	exvillaf@texaschildrens.org	Eva	Villafana
cdominguez@elpasohealth.com	cdominguez@elpasohealth.com	Celina	Dominguez
blesing_amazigo@uhc.com	blesing_amazigo@uhc.com	Blessing	Amazigo
akhil.raj@superiorhealthplan.com	akhil.raj@superiorhealthplan.com	Akhil	Raj
patsy.vrazel@bswhealth.org	patsy.vrazel@bswhealth.org	Patsy	Vrazel
jolynn@superhealthplan.com	jolynn@superhealthplan.com	Jordan	Lynn
thomas.moreland@superiorhealthplan.com	thomas.moreland@superiorhealthplan.com	Tommy	Moreland
Sara.D.Yepez@superiorhealthplan.com	Sara.D.Yepez@superiorhealthplan.com	Sara	Yepez
tam.donnelly@dchstx.org	tam.donnelly@dchstx.org	Tam	Donnelly
Nathan_Fortner@bcbstx.com	Nathan_Fortner@bcbstx.com	Nathan	Fortner
jennifer_housley@bcbstx.com	jennifer_housley@bcbstx.com	Jennifer	Housley
Xochil_zevallos@uhc.com	Xochil_zevallos@uhc.com	Xochil	Zevallos
Sheila_Strode@bcbsil.com	Sheila_Strode@bcbsil.com	Sheila	Strode
tracie.acosta@bswhealth.com	tracie.acosta@bswhealth.com	Tracie	Acosta
cristal.detert@bswhealth.org	cristal.detert@bswhealth.org	Cristal	Detert
Christine.Williams@cookchildrens.org	Christine.Williams@cookchildrens.org	Christine	Williams
Martinj4@aetna.com	Martinj4@aetna.com	Jenna	Martin
angela.guerrero@dchstx.org	angela.guerrero@dchstx.org	Angela	Guerrero
sabrina.heins@dchstx.org	sabrina.heins@dchstx.org	Sabrina	Heins
angela_moemeka@bcbstx.com	angela_moemeka@bcbstx.com	Angela	Moemeka
ALLISON.HAYS@COOKCHILDRENS.ORG	ALLISON.HAYS@COOKCHILDRENS.ORG	ALLISON	HAYS
jolene_bossier@bcbstx.com	jolene_bossier@bcbstx.com	Jolene	Bossier
Angela.Smith@cookchildrens.org	Angela.Smith@cookchildrens.org	Angela	Smith
mvnguyen2@ascension.org	mvnguyen2@ascension.org
carrianne.dockter@molinahealthcare.com	carrianne.dockter@molinahealthcare.com	Carrianne	Dockter
kwwhatl1@texaschildrens.org	kwwhatl1@texaschildrens.org	Krissy	Whatley
DL_CFHP_Regulatory@CFHP.com	DL_CFHP_Regulatory@CFHP.com	Community First Health Plans, Inc.	Community First Health Plans, Inc.
DL_Medicaid_TAHP_OPS@cfhp.com	DL_Medicaid_TAHP_OPS@cfhp.com	Community First Health Plans, Inc.	Community First Health Plans, Inc.
Carrianne.Dockter@MolinaHealthCare.com	Carrianne.Dockter@MolinaHealthCare.com	Carrianne	Dockter
brittany.hall@superiorhealthplan.com	brittany.hall@superiorhealthplan.com	Brittany	Hall
marivera@centene.com	marivera@centene.com	Manuel	Rivera
danita.steward@molinahealthcare.com	danita.steward@molinahealthcare.com	Danita	Steward
sowndharya_sunder@bcbstx.com	sowndharya_sunder@bcbstx.com	Sowndharya	Sunder
Araceli_Cappello@bcbstx.com	Araceli_Cappello@bcbstx.com	Araceli	Cappello
dominic_garcia@bcbstx.com	dominic_garcia@bcbstx.com	Dominic	Garcia
daimon.krumlauf@superiorhealthplan.com	daimon.krumlauf@superiorhealthplan.com	Daimon	Krumlauf
mespinoza@elpasohealth.com	mespinoza@elpasohealth.com	Nellie	Ontiveros
Hany.aziz@molinahealthcare.com	Hany.aziz@molinahealthcare.com	Hany	Aziz
victoria_cage@bcbstx.com	victoria_cage@bcbstx.com	Victoria	Cage
elizabeth_lade@bcbstx.com	elizabeth_lade@bcbstx.com	Elizabeth	Lade
plaso437@gmail.com	plaso437@gmail.com	Paul	Laso		Affiliate
Leeta.greer@molinahealthcare.com	Leeta.greer@molinahealthcare.com	Leeta	Greer
Jessica.mendoza2@superiorhealthplan.com	Jessica.mendoza2@superiorhealthplan.com	Jessica	Mendoza
kristy.bulhoes@bswhealth.org	kristy.bulhoes@bswhealth.org	Kristy	Bulhoes
tara.stafford@bswhealth.org	tara.stafford@bswhealth.org	Tara	Stafford
Laci.Noble@bswhealth.org	Laci.Noble@bswhealth.org	Laci	Noble
lucy.chibesa@bswhealth.org	lucy.chibesa@bswhealth.org	Lucy	Chibesa
AXTESKE@TEXASCHILDRENS.ORG	AXTESKE@TEXASCHILDRENS.ORG	AMY	TESKE
wendy.richerson@BSWHealth.org	wendy.richerson@BSWHealth.org	Wendy	Richerson
melissa.loper@bswhealth.org	melissa.loper@bswhealth.org	Melissa	Loper
marc.rains@cookchildrens.org	marc.rains@cookchildrens.org	Marc	Rains
Chevalier_DeShay@bcbstx.com	Chevalier_DeShay@bcbstx.com	Chevalier	DeShay
Lynn.Ramsey@dchstx.org	Lynn.Ramsey@dchstx.org	Lynn	Ramsey
james.locke@molinahealthcare.com	james.locke@molinahealthcare.com	Jim	Locke
jon.janovec@greatdentalplans.com	jon.janovec@greatdentalplans.com	Jon	Janovec
kevin.miller@dentaquest.com	kevin.miller@dentaquest.com	Kevin	Miller
mchapa@cfhp.com	mchapa@cfhp.com	Estela	Chapa
angela_kaiser@bcbstx.com	angela_kaiser@bcbstx.com	Angela	Kaiser
lisa.fillip@BSWHealth.org	lisa.fillip@BSWHealth.org	Lisa	Fillip
jserna@elpasohealth.com	jserna@elpasohealth.com	Jenette	Sera
courtney.mckevie@superiorhealthplan.com	courtney.mckevie@superiorhealthplan.com	Courtney	McKevie
Esther.Webb@BSWHealth.org	Esther.Webb@BSWHealth.org	Esther	Webb
lcrow@cfhp.com	lcrow@cfhp.com	Lisa	Crow
rkerr@elpasohealth.com	rkerr@elpasohealth.com	Ryan	Kerr
samuel.steinmetz@uhc.com	samuel.steinmetz@uhc.com	Samuel	Steinmetz
vera.martinez@cookchildrens.org	vera.martinez@cookchildrens.org	Vera	Martinez
REBECCA.BELMONT@COOKCHILDRENS.ORG	REBECCA.BELMONT@COOKCHILDRENS.ORG	Rebecca	Belmont
jennifer.boreing@bswhealth.org	jennifer.boreing@bswhealth.org	Jennifer	Boreing
Matt.Keppler@changehealthcare.com	Matt.Keppler@changehealthcare.com	Matt	Keppler	819	Affiliate
"""

# Combine the two input sets
combined_input_text = input_text_1 + input_text_2

# Parse the input and organize by ID starting from 645
user_info = {}
lines = combined_input_text.split('\n')
for line in lines:
    match = re.search(r'ID=(\d+)', line)
    if match:
        user_id = int(match.group(1))
        if user_id >= 645:
            # Extract the corresponding second string from input_text_2
            second_string = input_text_2.split('\n')[user_id - 645].split('\t')[-1]
            user_info[user_id] = f"{second_string}"

# Sort user_info by ID and display the ID and end of the second string
sorted_user_info = sorted(user_info.items(), key=lambda x: x[0])
for user_id, end_string in sorted_user_info:
    print(end_string)
