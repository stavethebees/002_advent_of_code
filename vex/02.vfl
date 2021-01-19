function string[] format(string input)
{
    string _output[];
    string _tokenized[] = split(input, "\n");
    foreach (string _s; _tokenized)
    {
          _s = strip(_s);
          append(_output, _s);
    }
    return _output;
}


// main
s[]@input = format(s@inputorig);
int _valid1 = 0;

for (int i = 0; i < len(@input); i++)
{
    string _output[] = re_split( r"\W+", @input[i], 0);
    string _queryregex = _output[2] + "{" + _output[0] + "," + _output[1] + "}";
    string _querystring = strip(_output[-1]);
    string _result[] = re_findall(_queryregex, _querystring);
    
    int _min = atoi(_output[0]);
    int _max = atoi(_output[1]);
    int _foundnumbers = len(find(_querystring, _output[2], 0, len(_output[-1])));
    if (_foundnumbers >= _min && _foundnumbers <= _max)
    {
        _valid1++;
    }
}
i@__resultPART1 = _valid1;


int _valid2 = 0;
for (int i = 0; i < len(@input); i++)
{
    string _output[] = re_split(r"\W+", @input[i], 0);
    int _min = atoi(_output[0]);
    int _max = atoi(_output[1]);
    string _searchchar = _output[2];
    _valid2 += ((_output[-1][_min - 1]) == _searchchar ^ (_output[-1][_max- 1]) == _searchchar);
}
i@__resultPART2 = _valid2;