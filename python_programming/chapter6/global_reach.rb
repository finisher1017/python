

def read_global
	print("From inside the local scope of read_global, value is #{$value}\n")
end

def shadow_global
	$value = -10
	print("From inside the local scope of shadow_global, value is #{$value}\n")
end



$value = 10
print("In the global scope, value has been set to #{$value}\n\n")

read_global()
print("Back in the global scope, value is still: #{$value}\n\n")

shadow_global()
print("Back in the global scope, value is still: #{$value}\n\n")