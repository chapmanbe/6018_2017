module quizzes


function literal_variables1(;arg1="replace_me1", arg2=0)
    try
        assert(typeof(arg1)==String)
    catch 
        return "arg1 is not a string"
    end
    try
        assert(arg1 == "327")
    catch
        return "arg1 is a string but is not the correct value"
    end
    try
        assert(typeof(arg2)==Int64)
    catch
        return "arg2 is not of the correct type"
    end
    try
        assert(arg2==327)
    catch
        return "The integer value of arg2 is not correct"
    end
    return "Your value seems to be correct."
end


function test_quadratic(myfunc)
    x = rand(-10:10)
    x0 = rand(-10:10)
    a = rand(-10:10)
    b = rand(-10:10)
    result =  myfunc(x,x0,a,b)
    if result == false
        return "Your function is not correct. Did you forget to set a value for y or explicitly return a value?"
    end
    try
        assert(typeof(result) <: Number)
    catch
        return "Your function is not returning a number."
    end
    try
        assert(result == (x-x0)^2 + a*x + b)
    catch
        return "Your function is returning a number but it is not the correct value."
    end
    return "Your function seems to be correct"

end 

function test_bmi(myfunc)
    mass = 15*randn() + 80
    height = 30*randn()+ 165

    result =  myfunc(mass, height)
    if ! (typeof(result) <: Number) 
        return "Your function is not correct. You are not returning a number. You are return a type $(typeof(result))"
    else 
        if result == mass/height^2
            return "Your function seems to be correct"
        else
            return "Your function is returning a number but it is not the correct value."
        end
    end

end


function test_pediatric_age(myfunc)

    function _ref(myage)
        if myage < 1
            return "NEONATES"
        elseif myage < 24
            return "INFANTS"
        elseif myage < 144
            return "CHILDREN"
        elseif myage < 12*16
            return "ADOLESCENTS"
        else
            return "OTHER"
        end
    end
    for i in 1:100
        age = rand(0:18*12)
        my_group = myfunc(age)
        ref_group = _ref(age)
        if !(typeof(my_group) <: String)
            return "Your function is not correct. You are not returning a string. You are return a type $(typeof(my_group))"
        else
            try
                assert(my_group == ref_group)
            catch
                return "You mapped the age $age to the group $my_group when the correct group was $ref_group"
            end
        end
    end
    return "Your function seems to be correct"
end

function test_random_integer(myfunc)
    result =  myfunc()
    results = []
    if !(typeof(result) <: Number)
        return "Your function is not correct. Instead of returning a number you are returning a $(typeof(result))"
    elseif !(typeof(result) <: Int64)
        return "Your function returns a number but it was not an unsigned integer"
    else
        for i in 1:1000
            result = myfunc()
            results = append!(results, result)
            try
                assert(20 <= result <= 50)
            catch:
                return "Your function returned an integer but the value $result is not in the specified range"
            end
        end
    end
    try
        assert(20 in results)
        assert(50 in results)
    catch
        return "You do not seem to have the correct range of numbers"
    end
    return "Your function seems to be correct"
end
   


function test_json()
    try
        assert(!(Pkg.installed("JSON")==nothing))
    catch
        return "JSON package is not installed"
    end
    return "JSON package is installed"
end

end
