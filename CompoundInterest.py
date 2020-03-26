P = input("Enter the Principle Amount:")
R = input("Rate Of Interest:")
N = input("No of Years")
F = P * (1 + R/float(100))**N
print "Principle Amount is : {:.2f} Rate of Interest is : {:.2f} No of years :{} Compound Interest is : {:.2f}".format(P,\
                                                                                                                        R,\
                                                                                                                        N,\
                                                                                                                        F)
