#include "scope_table.h"

class symbol_table {
private:
    scope_table *current_scope;
    int bucket_count;
    int current_scope_id;

public:
    // Constructor
    symbol_table(int bucket_count) : bucket_count(bucket_count), current_scope_id(1) {
        current_scope = new scope_table(bucket_count, current_scope_id, nullptr);
    }

    // Destructor
    ~symbol_table() {
        while (current_scope) {
            scope_table *temp = current_scope;
            current_scope = current_scope->get_parent_scope();
            delete temp;
        }
    }

    // Enter new scope
    void enter_scope() {
        current_scope = new scope_table(bucket_count, ++current_scope_id, current_scope);
    }

    // Exit current scope
    void exit_scope() {
        if (!current_scope) return;
        scope_table *parent = current_scope->get_parent_scope();
        delete current_scope;
        current_scope = parent;
    }

    // Insert symbol
    bool insert(symbol_info *symbol) {
        return current_scope ? current_scope->insert_in_scope(symbol) : false;
    }

    // Lookup symbol in all scopes
    symbol_info *lookup(symbol_info *symbol) {
        for (scope_table *temp = current_scope; temp; temp = temp->get_parent_scope()) {
            symbol_info *found = temp->lookup_in_scope(symbol);
            if (found) return found;
        }
        return nullptr;
    }

    // Print current scope and all parent scopes
    void print_current_scope() {
        if (!current_scope) return;
        outlog << "\n################################\n\n";
        for (scope_table *temp = current_scope; temp; temp = temp->get_parent_scope()) {
            temp->print_scope_table(outlog);
        }
        outlog << "################################\n\n";
    }

    // Print all scopes
    void print_all_scopes(ofstream &outlog) {
        outlog << "Symbol Table\n\n################################\n\n";
        for (scope_table *temp = current_scope; temp; temp = temp->get_parent_scope()) {
            temp->print_scope_table(outlog);
        }
        outlog << "################################\n";
    }

    // Get current scope ID
    int get_current_scope_id() { return current_scope_id; }

    // Check if in global scope
    bool is_global_scope() { return current_scope && !current_scope->get_parent_scope(); }

    // Lookup only in current scope
    symbol_info *lookup_current_scope(symbol_info *symbol) {
        return current_scope ? current_scope->lookup_in_scope(symbol) : nullptr;
    }
};