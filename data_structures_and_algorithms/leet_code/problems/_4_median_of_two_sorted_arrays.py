def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    for i, j in zip(nums1, nums2):
        if i < j:
            pass

    return ""


def findMedianSortedArraysNonEff(nums1, nums2):
    # Step 1: Merge arrays
    merged = []
    i, j = 0, 0

    # Compare and merge while both arrays have elements
    while i < len(nums1) and j < len(nums2):
        # Compare nums1[i] and nums2[j], add smaller to merged
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements from whichever array isn't finished

    merged += nums1[i:]
    merged += nums2[j:]

    # Step 2: Find median from merged array
    total_len = len(merged)
    if total_len % 2 == 1:
        # Odd length: return middle element
        return merged[int((total_len - 1) / 2)]
    else:
        # Even length: return average of two middle elements
        return (merged[int(total_len / 2 - 1)] + merged[int(total_len / 2)]) / 2


def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is shortest array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # We have ensured m < n
    m = len(nums1)
    n = len(nums2)

    # Binary search setup
    left = 0
    right = m

    while left <= right:
        # i = number of element to consider from nums1
        i = (left + right) // 2

        # j = number of elements from nums2
        j = (m + n + 1) // 2 - i

        # Implement checks
        # Greatest/last element from left partition of first array must be
        # smaller than the first element of the right partition of second array.

        # Address limit cases
        if i == 0:
            max_left_1 = float("-inf")  # No elements from left partition from nums1
        else:
            max_left_1 = nums1[i - 1]

        if j == 0:
            max_left_2 = float("-inf")  # No elements form left nums2 partition
        else:
            max_left_2 = nums2[j - 1]

        if i == m:
            min_right_1 = float("inf")  # No elements from right nums1 partition
        else:
            min_right_1 = nums1[i]

        if j == n:
            min_right_2 = float("inf")  # No elements from right nums2 partition
        else:
            min_right_2 = nums2[j]

        # Check conditions
        if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:

            if (m + n) % 2 == 0:
                max_left = max(max_left_1, max_left_2)
                min_right = min(min_right_1, min_right_2)
                return (min_right + max_left) / 2
            else:
                return max(max_left_1, max_left_2)
        else:
            # Update left/right
            if max_left_1 > min_right_2:
                # Too many i elements from nums1
                right = i - 1
            elif max_left_2 > min_right_1:
                # Too few elements from nums1
                left = i + 1


nums1 = [2, 3]
nums2 = [4, 5]
print(findMedianSortedArrays(nums1, nums2))
