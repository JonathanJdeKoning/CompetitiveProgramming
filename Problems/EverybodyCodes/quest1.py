# Part 1
s = "CAABCBCBAACAACCBACACBCABCBCBCACBACBCACBAABCBCBCAABCBACABBBCCCBCBABACCCCABABCBCCBBCBCCABACBBBBABBCBACBBACABBCCBABAACCCBCCCAABCAABBCABBAACAABBAABABBABABCABBABCBAACBCCBAAACCAABBAAAAABBCCCCAACCBCCAAACABCBCAABBACBBBCACACABABCBBACBBCABCCBCABCBCCABCACACACBABCABCCAACBCABAABCBABCCBACBCAACCCCACCCACCBACBCCACBCCCABAAAAAACAABCAABBCBBAAABBBABABCCBCCBCABBCBCBCAABBBCAABABABCBACBAACBCAABBCACBACACBCABBBCBBACACBCCBACBACCBBBCCBAACCCBBABCBBBABCACAABCCABBABCCABAAACBAABBABAACCCCABBBCACBBAAAABBBBABCAACBBBBACBBBCCBACCCCCACCCACACCACCBBBCAAACCBBABABCAACBAABBACBACCACABABBCACCABCACBCACAACBBACACCBCAAAAAABCCCABACAACBAABBCAAABCBACABCABBCACACBCACCBBBCBCBACCBACACABCABACCACBCABACABABCBBBAACBCBBACABBABCCAAABBBBBCAABCACCBABBCAABBBBBCACCABACBCBCBBCABABCCCABABBBBCBCAAABCCCACCCACAAAACAACAABBCBABCCCCABBCACBCAACCCACABAABBCACBABCBCBCCBCBACCBCABBCCCACBACABACAABABCACCACBABCCCBBCBCBCBBAAACCABCAAABBBABBCABBBCBBABBCCABBBAACCBCCCCABBCABABBCCBACCABAAABBAACABBBBACBCACABBABCBBAABCCAABAAACBBCBBABBACACBACBCABCCCABACCBBAACCABABBABBBAACABCA"
print(s.count("B") + s.count("C")*3)

# Part 2
s = "DBBCDAACBBDBBBADxDDxABxCDDDBCBCDCDAADCCCxACDDACCDDBCBCDCDxCCBxCAAACAAxxBDCAADBBDCDADxBCCBDABCCAAAxCBDADACBADAxAABCABCxCCADDBBDDDDDCDCDxCCxDDAxCBDDACDBBDDCCCBDxDBCBCACxxDxBADBBDAACDxCDCxCDBCCCCDDCDxCBCBCCDDDxCABAAAAAAxDxCxBCCAxDCCCAADCACDxADDABDCABCDDAADABCBCCBDCADCxCADCDCCDDDDCxCxBCBDBAxDxCBBBBCDBAxCCxDCCBDBCDDCDxACCxBDCBADAxxxCCCDDCxBBACBADADACDxDCDCDABCCAADCDCACADDxBxCADBDCDCABDBABCDACDCDBBDBBBDACCDDDDCDBCAxCAAACBBDBDxCBCBDBDBxCBxDxAABCxCBCBxDCCCBBADDCxCDCBDBxxxBxDCABCDBCBCCADCCCCDCADDACBBBBADAABADxCCDCxBAADBADABxADADAABBCxDADBBxBBDDAxDDCACAAxADCDCDxDAxCBACBBCAAAACCCDBBDABDCDDBCDxAACxAAAAxADAACCCCCABDxDBCBDBBBDBCBDDAxBABBCBCAAxxDBCxDABCDDCDACABxCDCDCADDDxCDDCABxAxAABBxADBCABBDBABDxAACCDCABxCBADAABCxACADCDDAxACACABBACCDDDBBxxDCCDDBABBDCCAxABACCBAxBCBDADCCCBCBCBAABDDxCAxBBDBCDDCxCDBDADDDDCDABDDAAxCAxBADCCCxCCCDAABACDDABxDDDAAAxBABCxDxADAABACBABABAxADCxACxCCDADDBADBCBDCDxBAABADDBDCBxBDBCCDCABDAAABABxCAADxAxBxCBBCDBCCDBCxDCBCxABBACBxBCDCABBBDBBADxCDDCDxBACxADAxBDBDAADDDxBxCBDADxCACxCACCDDxCCDxADBABBBACBCBCBDCxAADCACDDDCxDBBDDxDABDDCADADxxDADADADBDDADBDCDADDAADDADCBCADxDDDBBxACBBxAxCBDCBCBDBABBCBCBADCBACAxDADxCxABBBABACBADDCBADDDADADBAxCAADBCBCCCAxDCxABCACBABxCCCCCBCBAxBxCCAxDxBABBDBABxDDDDAxACDBCCCCDDACDDDBACDBABCBDDDDxBBBAAAABxBAAAxBBDCDCBDDDCDAADADAxAACBBABCAAxCBCADABBDCDxACCDABxAxCBxxADBCCBCDBDCCCDxDxxCBDCBABCxADAADAACCADxADCBBABCDCBDCDCBDDCDxxCBCACDACBAABCDBBxDDADDDABCDCDCxxCBDDCBCBxxCDDDBDBCDAAABBDAACCxDACCxCBBCCDDxCDBxABDCAxDxxCCDCACDDCABABDABxAxxBDCAACBACCCBCBBxADABDxCABBBxCABDCBxBBADCCBxBABACDCDDACxCDABCBDCACxxAABxCCCBDCBACBBDxCDDCxxCCDDBBDBxBxDxDBCxDBABCBACBDxDAxCCBDBxBBBxDAAxAxDBCxCADDAACADAABDDABxCCCBxCBCDDBDCAxBADCDAAADBDDBDCCCDDBCBxDACBxxBCxCCACDAACDCCCADBCCBCABDBxBDACDCADDDCCAABBAxBCBDBAAxDDBDBADDxAAACCDBxAAADDCBCxCABBDACxABABCADADCCCBBCBBDBCAACABADDCCDADAAxBBxDBCBDDBDxAAABCCDAABCBDAAACDBCDBDADxxAACDDBBCAxCBAxABBCBCDCACADCAxxDxxxxxxxCCCABCBBDADxACCxBBDBCBDBBCDCADDADDBBxABCxADBxACxBBACAADACDAACBCBCDBBCACxDAAxCCxDADDAAAAxxDADCDDAAABBCDACBxCDBABxDCCBCCxxCCA"
mp = {"A": 1, "B": 2, "C":4, "D":6, "x":-1}
ans = 0
for i in range(0,len(s), 2):
    a = s[i]
    b = s[i+1]
    if a=="x" and b=="x": continue
    ans += mp[a]
    ans += mp[b]
print(ans)

# Part 3
s= "CCxDxDBDCxxxxxxBCADACDCADDBDCBxDDCDABCADCABAxBBxDBxBxCxACDADxxDBxBBBDACBACDCCCACxBACDCCBABxAADxxBAxBBCCDCBADBDCCBxAACCxDCDDDxBCACCCxCBxDxCAACDxCDxxCxABCCBCCxBDCDBBBAxBBAxBCDBBBxCxBAACDxxBxDACCxCxABBBACAxAxCCCDxBxDADxDDDABxABBxACAxADCDCDxBCxABBCDADxDxAxABADDBBACBCAABxAxxBDCADDCDDxBABCxxACxACBAxCCBxAADCxCxDxADAACxCBCABxCBBBAABxCDBACCCBDxCDAAxCABAxCCACBAxAAxxDBABBxxCxACADABDxDxBBDDCDAxCDDDDxAxDADBABDBDCADDBBBBACDxDBxABCCxDACDDBBCBCxCxBDBBCBADDDxADCCBCCxACDDAAADCBCBCADDABAxBCABBBACDBACCAxBxCADDBxADxxADABBBCxABDCBxACABxCBADxCCDABCBCxCDxAxBCxBxDDCDACCCDxxxCAxCDCxxDBBxDxBxxCxBDDBCxCDCAACDxCDxxDABACDCBBAxABBxBxACBxADxxBBBCCBxCCDDCCBDCBBDBBCCDCxDAxCBxDBADCABADDAxBBDAxABBCADAxCBACCCDCAxxBDBBAxCBCBxAxDDBACBAADxBABADCCDACxxCxxAxCAABDDxBBBxAxDBADAADDBBDDAxDDBxBABCBACDBACDDBDxCCBACADDBABCBCCBBAAABxCxxxCACDBCBBxDABBxABxDxCDABDAAADCDAxCCCDBxxBBCDBBDDBxADACCACCAxCDBCxBDBBxCDxCDxDDxxDAxxABAAAxABADAxBCAABCBxBBBCDDBDBxBDCxxCAAxACDCAxDADCxCCCDCCDAxAxDDxCxACADBBDBDxBCxDxCDCDBxxBxDBBABACxxBDxCBxxDAxDDBDxCABDBxCBAAxAAAACCDDAxBxAADxCBAABBBCADCBxABABxBDBDDADBxxAACxBBxABCCBxxxxBDACCAxBACADxBxDDCxCDxCADxCABBDDCBxDCxDxBAAxBADBCDADCABACxBBDDAADCxCCxDABDDCxCABABAACCDCAADBxAxADBxxCABCABAAADDBCADCDBBxCDxDxDACxACCDxCDCACBBBCDBxDABxCDBCAxBxDxDCDCDAxBxDxxxCBCDDABCABxCDxBBADxBxDxCDCDDADxACxDxxBCCABCDACAxDABBDDCACCCCxBBDDBDCDBBBAAADxxCxDCDxAAAAAxDxCDDAxAxBBACDxCDDxCACCxCADDACDABDBxBDxADCxADDBACDDxADBxxABCBDDBDBDBDBxCDCxADBADBDCxDxADDBBABACBxBxDxxCCxBABxABAxxACxCDCDDDAxCDxBCBBCCxCAxCCACBxxCDDCAxCxCCBxDCDBCDBDxDxDCBCAABDDBCCADCBxCACDBBCCDDxBDCDxBBBCDBCCAxBAxAABDDBCxBCCBCxBDxBBDDBBxBBBCxDBBABABBDCCBCAxAxCCDACxDCBxxBBDBxCCxAxBCCAxBAxDxADxBBBCxBDBxCBxxCBDADxxDxCDxBxBBCCBCCCxCAxxBBxxxDADCCDDCCxCBxBxAAABCACxDDABCDCCxCACAABABCCxDDCBDACxBADCDCBBACDBDACDDADAAxACxDCBBDDCBDCABCCDBxxxDBxABxBCCAxBAxBxAxxBAxDBDxBBBCCCACDBCBAxABxDBxDDxCDCCBBABCDBCBBxACBDCCxDDCBBCABACCBABCxCAxBDxCAAACCDCxCDDBABDCBxDDCDDDBCDDCxCCxAABCDxAAAAxxDCAxCxDDCBDDABxxCBADxCxDxBBDBAABxCCCAABABCDxAxCCBDADxCCDADBAADxDBDBADDxAAxxCBBACDBBAxACACBBDAAxCCCCxCBBxABAACBDCCBACDDxDBBDBDDxxDDxDxxBxADCDCABxBDxxxBCACxxBCAxBDCDCAxDAxxCAACCBDxBBxxDxxBBCCCCCxDCAADxxxDBCCCCBBBBADCxCCxBAABDCCCCBDDBxBCCACDCDxDDDBCCCBBDCCAADxBADBCAxCBCCBCDxACBDDCDDBxAAACBBACACxBDAABxDACDxBCxDDBDxCBAxAxAxCxCBDCxxxDBxxxDDCACCABBAACDxAABxxDxACABBAADADCBxBxADBBACDCDCCBCCDxDABDDBxDDCxxDxBADBxxDCxBDBxBDxADCBxxACBDBABxxCCBxBDCDxBxCDxxBCBDBCDCBxxDAACxDxCxxxDDDxCCCxxDDDCDBABxABxBCCBxABDCDACxDAAxCBCCBDBBABCxDCBDACxDCCxxBDADCBADDADxCxCABCDCDDCBDCBCBCBADBCCACAABBAADCCCCDABBDxxAABAAADDDxADBABxBBxBBDCxDCCABBAACxDACDxCDDDABBxBDAxAxxBCDxxBDDxCAADxxxxBBxxCBADCBDCABBAxADCCxABxCCCDDDxxxBBCAxxACBDxxABCCAxABxCABCxCBBxxDBDBBDxxDCADABAxABBBCDxDBBxBBCADxABxDDBABDDAxDCDBCCAACBDCCBAxCBDxACxBxDCBBCBCDxDDCABCABDCACADCDBBACBCDDDxDBCAxBABCxABCxCCBBBDBABBBDBxDDDBDCAxCADxxDDBCAxBBxxABxABCDBxCAAxDDBxCABCCBCxxAABCBBDDxBxDAAABBCDACxBBBBxxBBxADxAxDxDxCCDDBCAxBxxCAxBDAxDDxDBACBDACxCBBDCxDDCxCBDCxCAAxAxAxDCxACDDBDxCCAxDCCBxBxDDxCACBAAxCBDDAAADABDADDxDBACAACAAxBxxBAxxxBBABCBDCBxxxxAxDxxADDxABDBCBACxBCBCCxCBBxBADBDBxCBxACCxxxCCxxBxxABCDACBAxAxCDxAAADBBxxCxDxDDxAACCDCxCBABxxABxxDCDBACxACDCACDBBBxAxDACDxBCACxBxDDBDDAADCAxADADCxDxDACBAAABCBBxBAAxBCxADDCxCCBAxDBAxCxADBBCCDDBxDxxABDxDABBDCDBBxADxDDDBDBxDABxxDCBxBCCAAxAxCAAxCDxxCxxDDACABBCDAACACDCAACBDBADDxBCxCCCCABBCDCAAABBDBDCDBBCBCDxxxxADBCBADAADCDDCADxBBDAABAxACDxDADBDCDCBxxxCDDBxBBCABCAxBBDDACCCCDBCCABCDBDCxABAAABACCABxBDAxxBxDDCBBDCxDDBCDBBCDBxBCBxBxDDAADCACBACDCDxxDBAAxABAxDxCAAxAAAAACCBCDBCCCxAxxDDDBBDACCxBxDACDAAxDxDBDDDCBxCBDDCxxxCDACCBBDBDxCDABDCABBAxBBDxDDxADCACBBDBAAABCCAABxABxCAxxxBCCBADDBBCCABBADBxBBxxBADCDxAxDAADBxxBCAxCDxDBCDxxBCDACAACCACBBDBBABDxBBAxxBDxACxDBAxxCAACxxxBCDxADADAxBCAADBBAADCDxCBCDCAAxCxABABCCCDxADxBCBCCCCDADCABCADAxxCAxDBBBDxxxDDDBBBDABBBxADCBxABAABDCBxBDxAACxxDBAABCDBBAxDxBDxDCxxxxDDBCACAADCAxCCACADABxCADBCBCxDBCDCCCAAxBAxCxCAAACxDABDxxDBBxxDAxABACAABACDxxBBBCBBBBCDxDCACDCBACxCCCDxBAxxBBACxCxxCDBCABBDCBxxACADDBDBCCDDCDDCAxAACDBCDBBDxDDADxDDACCBxxAxxDABAAACCCBCxADDAxABDBDxDDxDDBCBCDBBCBDAxDBACxxxADAABDCxAADDADxDBCCBxCADABCxxACCDAABBxBDxBAABCADDxBCDxBDAxDDDxADCAAAxBDBCDBAxACCxDBxCCxDxADDxxAxADDADABBABxDxAADCDxxxxDABAxAxDBxDxBxBDxABBCACBDxBAABCBDBBxCCADBADxCBDADABCBDACBDBAABxBCxBADACADxABCBCCDxCxDxxAxCxCCxDCCABDxDADDDDAAxABBxAxxCDBCBxxDCxxACxxCDCxAADxBBxBAxDABBAxABAxBxCCBDBDBDxxCABDDCxAACBxBCxBDxBCDCDADCxBADDDDCDxCCxBBBBxAAABxBBBxAABDDxDBCAADDxxBCxxDxCCBCDCBCDDCCACABDDBDCxCDAADxCDBBxADCDxBDxBCADABCACxDCBBADCCACDxACDAxxxCDBAxBBBxDADADCBDCDBBxAxADBDCxxCDxDBCCBxDxBCABCxBxxBDDBxABADxAxCDCBACBxBCCACCABBBDBDCxDDBDxDADAAAABBBBAxCBCBxDxCBxBCDDBBxAxxDxDDBCxDACACDDxAADxABADCDDxDADDxDxxDDCBCABDBCDAxBxCxBxCxxBDAxABxxDDDACABBBxDBxCxBDxAxADCADADADDCxCBBBxxAxDBxxxAABxxxBDACABxAAAAxDxBCDxxxxADxxxDBCCDCDDxBDCBDBCxDDABxxxAACAxCADCDBDBBCAxDxBBxCxxCAABDCCxAAACBAxBDAAxABCADABDCABxAxABxxBCAxxCBxACxCBCBAxAABABBDDAACDxCCBCBCAxAAAxCDBACxxDAxCxCBxCABxDAADCBACAACCDDDBADxBABBDxABAxCDDCBBDxCCBACCDCxADABDCAxBDxCBABAxBxCADDCDCDDxxACDCCCxCABxxDxADCACCBxBDCAxxxBDxADACCAAxAxCDDBDBAxCDAxDDxBDCBBBCBDAxBDCDADAxBAxDBCxDBBCCDCBBADBCDDCxxABxCDBBDDBCAxBDCABCCADABCxxDCDAACBBxxDCBAxDCABxBCCxxDDACDCDBBDxBCxBABDAxCBCADAxACADBxxAAAACCADBxxCBCCAxADAADCCACBDACBDAxBBxBACxxxDDDCDDCBCxCCDDDDDDCACDDCAxxAxABxAACADxDACABCABDDDxAxxCBBxACCADBCBBBBBADxAACADCDDACxACAxCxxCAxDADDDBBxADBCABBDDDAAxCBDCBDAAxAAACDCxBBBBBxBBBDBADxABBACDBADxCxBxxDCBCBCCxBADCABDDBDBBxCDDxDxBxCxCBBBxBAxABCCDADAADABBCDADxDDCxBDDABxxADAxAABxBDABCxBBDDDCxDxxCAADACxxCDDCAACxCABADBBCxDDABxBCDxCADxCAxAxDDDDxBCxCBDDxxBCxDDDCDxDACCAAABADxxADACDBBDAACCxxAxBxCBCxAxCDBAxCDxCDAADxBDAxBxCBABCBADCACBCCDDxxBDAxCBDBAxACABxDxDDBxCADxDCDxDxxxCDDABxDABAxxDxxDDDDCxCxBDABCDxDxDBBBxCCADBxDACxCBBCACAACDCCCDACCBDCDCAACAxBBCCxBBxABDDxxCCCxBCCAAxxxDBDADACBDABxADDCxCxDCCCCBAAADAAxACCDDBBBCDACACxBxDDBDDxBACCBxCBBDCACBAxxDxDDDBxCCCCCCABBDxAxBxCDBCCDABCCABCCAxDxCCDDACDBBBDBADxDCBCACBCCBABAxCBDDBxAxBxBBCBCCDADxxBxDABDxABCBACDxCxBDDABACCCDCxxBxDACCBABDDxCxCCxxxxBDxBDABCCxBDDDBBCCBACCAACDxACBCxBADxxxABxABxDBxDxCCDBCCACBBxDCCCxBxDAxDDBACCABCCDCACBxCCABxCAxDxBxCADBxxDDAxDADBACAADABBDxDBAxDAAxDDCxBxAABCABBBCDxAxBBBBBDDBADBBBDACCDCCxDxxBBABxDDBDDCxAxDCBAxADBDxDBBCBCBxDDxBABxxBDxxCDxxACBxCACxCDCDBABDABDABCCBCDBACCDDADDxADAAAACDABAAAABxxxAAxDBAABxDxBAxxCACDDCxDDADDBAxDBBDCxxABCACACxBBBCBCDBxDDBAABABCDCBABDBCxBDAxCDDBxxBBACACAxDDCBCADABABCDBCCAxAABDxACBBBCxAxBDACCBCBAADADCDxADDDBBCBxBDBCDDBBxCDACCCxCCCDAACDADxDAAxCBCDxCCDCxCACCDDBxDxDCCAxCxCBCDDxBAxBBCCBxACDBCCBCBBACABAxAxADDACBBADxxACACADDxxCAxADACBDCBBCBABBBCDDDxxBxxACCDCDBADDxDxBADBxDDDDAxxBBxABDABBxCBBxADBxCDAABCDBCxDCxxDxxCxxABCDABDxDDxxDxBAACxCAADDBADxxxBCCxDDABAxBCCADxBACAxDBBACBDCDxADDDBCADxCAADCCDCBDxCCDxCCxABxBADxBxDBBACBCxDxBxxDDCBDCxBDADDACCxBDCBDDDCDxDDDBBDDBCBADAABDADBBBxBxAxCBxBAxBCxxxAxDBxCCBBDADBDBBDDDCBBxCCxCBCCCAAxDABxCCxxCBBABACDxACABxDBBADAAABxBDxxDxAACxBAAAABBACABDDCBDAABDxxDAADBxCxCBxxCxxDDAADADxDAAxCxBAAxBxCACBCBBCAAAACCACACACDxBCDDDxCDBACDDDCAABBAAxCxBBDDxDCDDxDxCBAxADxxxADDDDBCCDDxABABBADDxDACCxAACAADxACADCAxBDAxDAxxDxDBBAxxBCxADCDCBCACDADDDAxDAACADCDAAxAxCDDxAACCxACCxCCxCBDCBDAxCCBxDxDACAADxCADxDCDxCDBBBDxxDDxCBBxxCDxCCBDCBDDABCxCCBBAxBCAxAxDCCCBBBCCBDCxBCCBDAxDCCDCxAAxBDCBBBAACBDAAADxCADxAxAxBDACAxDDCBBxCxCCCCxBDBADAACDCDDAxCBBAAABDBDAACxxCADBDBxBBBCBABDxACDDBDDABxCABAAABBCDAxDxAxxDAxxDBBDCxADDDDxBBAABADCxCDCABCBxDABxBDCxDBCDADCCDBDDxCAxADxCxCBADBxxDAADCACBxAxDCDCBCCCADxABCDBDBDBCBBCAxBBDDBBxCDACDDCCDxxCBCxxACxBxBDDDACACBADABxADCDDADBABCCBAABxxAAAxxxxBCCCCDCxxBCBABxCABxCxBxCxxBDxCCxDBDBADDBCDAAAxxCAxDCAxCABCACBCBADxBCACCBxDxDBADxAAADDBDCxxCxBCBCCCABBxBDDBCABABxxCBDCBACCACDBBBCAxBABDDBCCDAxDBBACCCBDxCxAxDxAABCCACACCBDDDAxBDDCBCACAACDBDCCAxDCACDDBDBABBCABxBBDBDBACxDxCBBACDCAADBxADDDxxxBBBBCBCxBxBDDADDxBCDCBDABACCAxDDAxAAABADDAxBxDBxBxDDDADAAxxxABDxBCAADAACABAxDxCDDBDCBCBxxCCDADDABDBCBDADxDCACDxBBCCADAxCBCDDBDDABAAAADCCCxxxxCAAxDCxxAxBDDxACBBBBBxAxxDBABBCCxxADDAADDBxCCxDxABBBCxADxDBBADxAxCAxAAAxDBCxDDxDBxxCCBBxxxxBCADBAxADDDACxxCxAADCxAAACDDBAACABxBCxxxADCxBCBBACCDBDDADADDxxCxxADDBBBCxxCBxADDABDDDDADADCBDCCxxDCxDDCCBxBCBAAAxDDACxADxADCCBDACxBBCADCDBCDBCADAxAAAABxCDAABDBABBxxDCCxDxAxBDDABxCDCCxCxBxCCACCCDxDDBAxxAxAxCBADDDAAACCBDAACDBBBDBDxCBBBxCBCxCACADDAAADDDDCBxABBxBAxAxxCxBxCAxAxCxDDBxBCxBCxCDxDAxDCxDACBDCBADCxBBDDBxCBxxxDxBDxBCCADBxCBCCxACBxxCBDADCBAxxCxxAxAABACxBCCxACBDBDDDADBBBBBCCDxBDAADDDACDBABBBCCxABDABABBxDAxDADxCBDBDAAxCBADBBBDCxADAAxDDBDxBBDBDBxCAAxDADxBxBCBAxBAAAxCxDDABADCBBABBCCBxBxACABCACDABDBDxADCAxCCxDxCCACxBAADDBxCCBCBDDCDxBBBDABCCxDCDACDDACACCBAAxDCCDxBABABAxACDBCBABAACCDDBBABDADACxDDDACBCDxBxDxCCBDCCBACCBxBABxBCAAxACBCDxBxCDDxDABBxxBBBxABCxxCxADAxBDBDACCCABxAABADCCBADCDADCADCDAxDDDBBCCBBCBBxABBBxxxDCBCDAxADxCxDAAxBBxCxCACBxxCxBCBxBACCxxACDABCBxBDxDAAAxxCBACDBBABBBxxBBBABxDxxxCABBDABDACAxCAxxCCxBAAxDCBCBAABCBxBBBCxDxDABABACDxDxADBACDACDCBCCDCxCDCADBCxxABxCCBCDAxBDCACCADCAADADBxBAxBDxACBACBADAAxAxxBxBDBDBDACxBCDCDBCxxCDBCBxxAABxCxBCCDDBDADCxCCCxxDDxDACBBABxADBxDDDxxCDDDxDxBxBAADCDCABDxCDBBxBxxDAxxCDBBxCAAABBDBDxxCBABAADCxAxxxDDACCxxCBxABBCADACCxBCBABDCDADABCCDBAABBCxDBxxCBBDxDABBABBABxCCCBADCBDxBxxAAxDAACDBxADBCBDACBBBBCDCDCAxxDCADDADACxCCCxxxD"
ans = 0
mp = {"A": 0, "B": 1, "C":3, "D":5}
for i in range(0, len(s), 3):
    a,b,c = s[i], s[i+1], s[i+2]
    bugs = [x for x in [a,b,c] if x != "x"]
    if not bugs: continue
    if len(bugs) == 1:
        ans += mp[bugs[0]]
    elif len(bugs) == 2:
        ans += 1 + mp[bugs[0]]
        ans += 1 + mp[bugs[1]]
    elif len(bugs) == 3:
        ans += 2 + mp[bugs[0]]
        ans += 2 + mp[bugs[1]]
        ans += 2 + mp[bugs[2]]
print(ans)