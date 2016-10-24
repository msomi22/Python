function canIWatch(age){
	if(age >0 && age < 6){
		return 'You are not allowed to watch Deadpool after 6.00pm.';
	}
	else if (age >= 6 && age < 17) {
       return 'You must be accompanied by a guardian who is 21 or older.';
	}
	else if (age >= 17 && age < 25) {
       return 'You are allowed to watch Deadpool, right after you show some ID.';
	}
	else if (age >= 25) {
       return 'Yay! You can watch Deadpool with no strings attached!';
	}
	else{
		return 'Invalid age.';
	}
}


describe('canIWatch tests', function () {
  it('Should return the appropriate message for age less than 6', function () {
    expect(canIWatch(5)).toEqual('You are not allowed to watch Deadpool after 6.00pm.');
  });

  it('Should return the appropriate message for age less than 17', function () {
    expect(canIWatch(15)).toEqual('You must be accompanied by a guardian who is 21 or older.');
  });

  it('Should return the appropriate message for age less than 25', function () {
    expect(canIWatch(20)).toEqual('You are allowed to watch Deadpool, right after you show some ID.');
  });

  it('Should return the appropriate message for age above 25 than 6', function () {
    expect(canIWatch(30)).toEqual('Yay! You can watch Deadpool with no strings attached!');
  });

  it('should return an appropriate message if provided age is invalid', function () {
    expect(canIWatch(-1)).toEqual('Invalid age.');
  });
});