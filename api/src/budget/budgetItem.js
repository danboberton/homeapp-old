class budgetItem{

    constructor(date, dollars, cents, description, category) {
        this._date = date;
        this._dollars = dollars;
        this._cents = cents;
        this._description = description;
        this._category = category;
    }

    get date() {
        return this._date;
    }

    set date(value) {
        this._date = value;
    }

    get dollars() {
        return this._dollars;
    }

    set dollars(value) {
        this._dollars = value;
    }

    get cents() {
        return this._cents;
    }

    set cents(value) {
        this._cents = value;
    }

    get description() {
        return this._description;
    }

    set description(value) {
        this._description = value;
    }

    get category() {
        return this._category;
    }

    set category(value) {
        this._category = value;
    }


}