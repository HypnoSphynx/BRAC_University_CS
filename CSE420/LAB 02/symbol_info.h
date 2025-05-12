#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

class symbol_info {
private:
    string name;
    string type;
    symbol_info *next = nullptr;
    
    string data_type;
    bool is_array = false;
    int array_size = 0;

    bool is_function = false;
    string return_type;
    vector<pair<string, string>> parameters;

public:
    // Default constructor
    symbol_info() = default;

    // Constructors
    symbol_info(string name, string type) : name(name), type(type) {}
    
    symbol_info(string name, string type, string data_type)
        : name(name), type(type), data_type(data_type) {}
    
    symbol_info(string name, string type, string data_type, int array_size)
        : name(name), type(type), data_type(data_type), array_size(array_size), is_array(true) {}
    
    symbol_info(string name, string type, string return_type, vector<pair<string, string>> params)
        : name(name), type(type), return_type(return_type), parameters(params), is_function(true) {}

    // Getters
    string getname() const { return name; }
    string gettype() const { return type; }
    symbol_info *getnext() const { return next; }
    string get_data_type() const { return data_type; }
    bool get_is_array() const { return is_array; }
    int get_array_size() const { return array_size; }
    bool get_is_function() const { return is_function; }
    string get_return_type() const { return return_type; }
    vector<pair<string, string>> get_parameters() const { return parameters; }

    // Setters
    void setname(const string &name) { this->name = name; }
    void settype(const string &type) { this->type = type; }
    void setnext(symbol_info *next) { this->next = next; }
    void set_data_type(const string &data_type) { this->data_type = data_type; }
    void set_array_size(int size) { this->array_size = size; this->is_array = true; }
    void set_as_function(const string &return_type, const vector<pair<string, string>> &params) {
        this->is_function = true;
        this->return_type = return_type;
        this->parameters = params;
    }

    // Destructor
    ~symbol_info() { delete next; }
};
