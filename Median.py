class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        meio = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:     
            i = (l + r) // 2
            j = meio - i - 2

            Aesq = A[i] if i >= 0 else float("-infinity")
            Adir = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Besq = B[j] if j >= 0 else float("-infinity")
            Bdir = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aesq <= Bdir and Besq <= Adir:
               
                if total % 2 == 1:
                    return min(Adir, Bdir)

                return (max(Aesq, Besq) + min(Adir, Bdir)) / 2
            elif Aesq > Bdir:
                r = i - 1
            else:
                l = i + 1


                
