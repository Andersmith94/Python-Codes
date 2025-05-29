def get_cut():
    cut = input("\nThere are 3 wires. Red, Blue, and Green. Which one should the private cut? ").strip().lower()
    if cut == 'red' or cut == 'blue' or cut == 'green':
        return cut
    else:
        print("\nShaking, the private reaches forward with his tool until...\nPRIVATE - OH SHIT my hand slipped! \nBoom "
              "\nThe private suffers a violent and nasty death.")
        exit()

def cut_wire():
    cut = get_cut()
    if cut == "red":
        print("The private reaches forward and snips the wire. The device beeps loudly, and is silent. The flashing light goes dark."
              "\nSERGEANT BUCKSHOT - Congratulations soldier! The bomb has been diffused. I have a feeling you'll fit in "
              "just fine here")
    else:
        print("\nBoom \nThe private suffers a violent and nasty death.")
        exit()

def story():
    print("While I was sleeping last night... er, I mean on guard duty... the enemy somehow slipped into our camp and \n"
          "planted a bomb in the lavatory. Go in there and disarm it! \n"
          "\nSergeant Buckshot shoves a pair of wire cutters into the the private's hands and shoves him toward the worn down shack. \n"
          "The private hesitantly makes his way into the lavatory. Filthy, crawling with roaches, and definitely not up to military standard. \n"
          "Poking out of a crusted toilet are colorful strands of wire, which upon further inspection are part of what \n"
          "appears to be an explosive device. A large yellow light flashes dangerously in the center.")
    cut_wire()

def main():
    print("SERGEANT BUCKSHOT - Hello private! Welcome to the warzone. You're just in time to join the action! Now tell me soldier...")
    get_experience()

def get_experience():
    experience = input("Have you ever diffused a bomb before? - YES/NO: ").strip().lower()
    if experience == 'yes':
        print("SERGEANT BUCKSHOT - 'Outstanding!")
        story()
    elif experience == 'no':
        print("SERGEANT BUCKSHOT - Well then it's about time you learned!")
        story()
    else:
        print("YES OR NO SOLDIER!")
        get_experience()




if __name__ == "__main__":
    main()