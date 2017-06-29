#!/usr/bin/python

from lantern.modules import vigenere
from lantern.analysis import frequency
from lantern.fitness import ChiSquared

ciphertext = """HNQDLVYOPOKFACCEKYATQNEPPTUKPCVVGBXYLPCZIIZTGORRNETKVILSVOHZUCQWTLAETMVZTEUMEEKANRETRETKVILSVOHRMTGBFRUKVKQGLRKXKUHMPUMUZTJOCILANVECPKGLYKKIFISLPNAYYIAHTOIGPEEOTJFCJYPFNYCXHJAEERRFIRCSRVCETDEBLANYSBIEJSRUAHGOCVZOHDLVOAEUIIKIFISLLVGBAFUDGBAYHTOKHVOIODMTRWJKXWVREOWJOAROHYPMYREKTAAREMLMQVHVKHKWMRTAJKGBLRGXXVYMAGSISDOSRVPSCGSISDVREKIEISRJDIVRWTOOQVMDZMCBXVYTJKRDVSVYJKOEQDLVYKKNWKOIUMVRWTJOCKLAERYJIOTOWDLDCWRLUDGBETOIGFIIAHGIVVHLNKPZREKWMEQUPSSIOIIRSIOIIRWTOOQVMMLLKCXVUEFDSKLAERIIZEZZPRPNHYVKOEHSJKLEPDLKPMGRSNAOTOHLJECPVRJTKYRZBNFOVJAAPNMKUOOCWDPTJSHZKNVCLFDMAGSIRIFSHZAIPWCYLAFNEDUKKNTIVBCLPPJORSIUPTVRIPYECVPRSIMOMDHDGKHZZCQFIIFTQNEPPFQERUHCQWTLAETGEZAAUOGFUDVRMJPSEYSCPTFYIJDHCDMNHNVSXKVIHSXDHKGCEDPSVKOVPTULITHUUOMJJRGGIUPTWZRFABGMELZEKDHFLSPDPZREOOSIMEGVWKORGKXVUEFLCDLOTDLZUKUSQRZMCBXRZSQBHFLSPDPZREVOETOIPQEEKSJYYCKNVLIYLRGNEDUKKNECSHGNSVZIUZPRFGCWIJAHGIVVHLNKPZRECXHKOEPSXYHPRORVKAFYSIVPGXIUAOCGSISDTEWYPNIDLIVUIRXYLPJYRVSIPOPZREJOVFPNVRVFBGJKRRKDKMXJCEKXWRUENOGKYOPSGGBLUOMJZEPDSLAATOJLNEHBSDAHGNEPAOFKCZUCQWTVAEPMMVZIUCSLNHVKFFHRFSWWVUPNXYPSKCMKAHKCMJDHGBIZIENYRXPKPYAVCETISELHGBIVCEPSJZCEPOZVYMGDXYLMPOZVYTCVOVKTQDLVTMCIRVCETRIRYFTYQKOEOKKRPNKURFDYQEECSDCWRBPDVIMENURDLVWHQXICPNGKKRPNVRIPYECVPRSIMOCFBBGDCFBRCCWNLRGKPCHLKUINLVGLIVUSRYSEMEFLESFFQYHRASERSFSWJORNLHWXKVYEFPSIZTGKOKOEDSXJVFOOEKAHCDCFBDKNPVASNSTKORQEKYDETOTILCJOAVKAPNXRZTGVIJZWGFISLEPNSDPNCDIUIYUKHZZTUYVZNNQBIUIYVRIRWAVRIKPCVRIWLWVREKOAFCSDLTJSRXAOVOETOFQERUBSYSPCPNIZYGPLULYKAHQCIWLWCBICPKGNVFWSQPARAETSRKOEFOWVYTVRMJPSQEVNVRNNRFDTJOAFYLFYJKOEGVITARQXEEKTJOWNPTERXYLBGKYKFOHDLVIAWNAVTAMOYJLOHKWVYVKMIRSRGKHPLXKCXZUGYSXYVUVZEPPNIPSIDHCDGFBLFLIUPRVMLVHPKPMKDAUXXIBNDITIVFKDIVYIPQKCBTVYRJHNFISLJANVYJJRKWMEHLUGIVEPNYVVHNFISLJANVYJJRKWMEHLUGIJLEMKJKLRMXSNSEFQIRUDAYYTHLNEWTYIOSRRSSYOIOPSVGMKOOWDWBPNEYPFYWKDLFBTPKXZVNCVMKFWKDLFBTTOPZNIQEWSPAUKRUFOWMECSUUMVZTIPKPJFOWLYZSDCDSDPCDYQSZYQEARNEYKVJFOWWYIKETMLVHTCXHCPEVYYJHNFDVPAOOKOVBSDOPZLVGSXJMOTYYIVWPQSFKYGDAVYEVRITYIOSRRSSAOWZHMCMVZTIPKPDFCTSQVPSVREKVFEEVZVSKDCDFCTSQVPSVREKVFLEHXPNIZIFWLGLCNOAVDLVFSCIEEKTJSRBUOVGLRATJOCCVOMVMBLMAMVZTEKCXYHTQPSLASOKVKPNIISLZOOOXYPNIDLRAYQEAZSLPOZVYFQBKZCEOOJFYICWEYHCMOVRUDVRMJPSOIQRUIHOWKVYQEQRFSVYTKOIUSRUPVKNYRSBWDCFBCCXXJAOREWRSLCPXVYANVAVYECVPRSIMO"""

decryptions = vigenere.crack(ciphertext, ChiSquared(frequency.english.unigrams))
print(decryptions[0])
