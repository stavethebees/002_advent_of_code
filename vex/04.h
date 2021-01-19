function string[] format(const string input[])
{
    string _output[];
    foreach(string _s; input)
    {
          _s = strip(_s);
          _s = re_replace(r"\n\s{3}", "", _s);
          append(_output, _s);
    }
    return _output;
}


function string[] reduce(const string input[])
{   
    string  _output[];
    foreach(string _s; input)
    {
        if(len(_s) != 0) push(_output, _s);
    }
    return _output;
}


function int testfieldregex(const string field; const string regex)
{
    return re_match(regex, field) > 0;
}


function string keeponlyfields(string input[])
{   
    string _output = "";
    foreach(int idx; string _s; input)
    {
        if(idx % 2 == 0) _output += _s + " ";
    }
    return _output;
}


//main
string _fields = r"ecl|pid|eyr|hcl|byr|iyr|hgt";
string _regex = r"\n    \n";
s[]@result1 = format(re_split(_regex, s@inputorig, 0));
string _regex1 = r"\W";
int _valid = 0;

foreach(int i; string _s; @result1)
{

    string _result2[] = re_split(_regex1, @result1[i]);
    string _result3[] = reduce(_result2);
    string _result4 = keeponlyfields(_result3);
    string _result5[] = re_findall(_fields,_result4);
    int _result5length = len(_result5);
    if (_result5length == 7) _valid++;
}
i@__resultPART1 = _valid;


int _valid2 = 0;
foreach(int i; string _s; @result1)
{
    s[]@result2 = re_split(r"[^#\w]", @result1[i]);
    
    s[]@_keys = @result2[::2];    
    s[]@_values = @result2[1::2];
    
    int _country = find(@_keys, "cid");
    removeindex(@_keys, _country);
    removeindex(@_values, _country);
    
    if (len(@_keys) < 7) 
        continue;
    
    int _sortorder[] = argsort(@_keys);
    @_keys = reorder(@_keys, _sortorder);
    @_values = reorder(@_values, _sortorder);
    
    int _byr = testfieldregex(@_values[0], r"(19[2-9][0-9]|200[0-2])");
    int _ecl = testfieldregex(@_values[1], r"(amb|blu|brn|gry|grn|hzl|oth)");
    int _eyr = testfieldregex(@_values[2], r"202[0-9]|2030");
    int _hcl = testfieldregex(@_values[3], r"#[0-9a-f]{6}");
    int _hgt = testfieldregex(@_values[4], r"(((1[5-8][0-9])|(19[0-3]))cm)|((59|6[0-9]|7[0-6]))in");
    int _iyr = testfieldregex(@_values[5], r"201[0-9]|2020");
    int _pid = testfieldregex(@_values[6], r"[0-9]{9}");
    
    _valid2 += _byr & _ecl & _eyr & _hcl & _hgt & _iyr & _pid;
}
i@__resultPART2 = _valid2;