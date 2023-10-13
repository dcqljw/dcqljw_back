export default function signOut(this_) {
    localStorage.clear()
    this_.$router.push('/')
}