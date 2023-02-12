// We need a function that can transform a number (integer) into a string.
// What ways of achieving this do you know?
// Examples (input --> output):
// 123  --> "123"
// 999  --> "999"

// We need a function that can transform a string into a number. What ways of achieving this do you know?
// Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
// Examples:
// "1234" --> 1234
// "605"  --> 605

void main() {
  //
}

String numberToString(int value) {
  return value.toString();
}

int? stringToNumber(String value) {
  return int.tryParse(value) ?? -1;
}
