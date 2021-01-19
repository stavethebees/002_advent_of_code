function string[] format(const string input[])
{
    string _output[];
    foreach(string _s; input)
    {
          _s = strip(_s);
          _s = re_replace(r"\n", "", _s);
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


// main
s[]@result0 = re_split(r"\n    ", s@inputorig, 0)[1:];
s[]@bag_array;
string _searchbag = "shiny_gold";

// populate attribs
foreach(string _s; @result0)
{
    string _result1 = re_replace(r"(\sbags?[,.]?(\scontain)?(\sno\s\other)?)|\s\d", "", _s);
    s@result1 = _result1;
    string _result2 = re_replace(r"(\w+)\s(\w+)", r"\1_\2", _result1);
    string _result3[] = split(_result2, " ");
    string _bag = _result3[0];
    if (_bag != _searchbag)
    {
        setdetailattrib(0, _bag, _result3[1:]);
        push(@bag_array, _bag);
    }
}

// in another wrangle
string _searchbag = "shiny_gold";
s[]@bag_found_list;
s[]@bag_parents;
int _found = 0;

push(@bag_parents, _searchbag);

while (len(@bag_parents) > 0)
{
    foreach(string _bag; s[]@bag_array)
    {
        if (_searchbag == _bag) continue;
        string _bag_list[] = detail(0, _bag);
        if (find(_bag_list, _searchbag) > -1 && find(@bag_found_list, _bag) < 0) 
        {
            push(@bag_parents, _bag);  
            push(@bag_found_list, _bag);
            _found++;
        } 
    }
    _searchbag = pop(@bag_parents);
} 
i@__resultPART1 = _found;