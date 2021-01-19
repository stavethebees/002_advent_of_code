function string[] format(const string input)
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


function string[] format(const string input[])
{
    string _output[];
    foreach(string _s; input)
    {
          _s = strip(_s);
          _s = re_replace(r"\W", "", _s, 0);
          append(_output, _s);
    }
    return _output;
}


void add_to_alphabet_array(const string input[]; int alpha_array[])
{
    resize(alpha_array, 26);
    foreach(string _s; input)
    {
        // go thru each char
        foreach(string _ss; _s)
        {
            int _pos = ord(_ss) - 97;
            alpha_array[_pos] += 1;
        }
    }
}


function string returnunique(const string input)
{
    string _result = "";
    foreach(string _s; input)
    {
        if (find(_result, _s) < 0)
            append(_result, _s);
    }
    return _result;
}


//main 
int _valid = 0;
string _result0[] = re_split(r"\n    \n", s@inputorig, 0);
string _result1[] = format(_result0);
int _sum = 0;
foreach (string _s; _result1)
{
    _sum += len(returnunique(_s));
}
i@__resultPART1 = _sum;


foreach (string _s; _result0)
{
    int _alphaarray_entries[] = array();
    string _result1[] = re_split(r"\W+", strip(_s), 0);
    add_to_alphabet_array(_result1, _alphaarray_entries);
    int _people = len(_result1);
    int _validresults[] = find(_alphaarray_entries, _people, 0, 26);
    _valid += len(_validresults);
}
i@__resultPART2 = _valid;